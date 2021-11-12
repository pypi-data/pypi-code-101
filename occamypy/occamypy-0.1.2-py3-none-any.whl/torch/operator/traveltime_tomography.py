import numpy as np
import torch
from occamypy import Operator
from typing import Iterable, List, Tuple, Union

Tensor = torch.Tensor
Shape = Union[List[int], Tuple[int, ...], torch.Size]


def ravel_multi_index(coords: Tensor, shape: Shape) -> Tensor:
    r"""Converts a tensor of coordinate vectors into a tensor of flat indices.
    This is a `torch` implementation of `numpy.ravel_multi_index`.
    Args:
        coords: A tensor of coordinate vectors, (*, D).
        shape: The source shape.
    Returns:
        The raveled indices, (*,).
    """
    
    coef = coords.new_tensor(shape[1:] + (1,))
    coef = coef.flipud().cumprod(0).flipud()
    
    if coords.is_cuda and not coords.is_floating_point():
        return (coords * coef).sum(dim=-1)
    else:
        return coords @ coef


def unravel_index(indices: Tensor, shape: Shape) -> Tensor:
    r"""Converts a tensor of flat indices into a tensor of coordinate vectors.
    This is a `torch` implementation of `numpy.unravel_index`.
    Args:
        indices: A tensor of flat indices, (*,).
        shape: The target shape.
    Returns:
        The unraveled coordinates, (*, D).
    """
    
    coords = []
    
    for dim in reversed(shape):
        coords.append(indices % dim)
        indices = indices // dim
    
    coords = torch.stack(coords[::-1], dim=-1)
    
    return coords


def sorting2D(tt: Tensor, idx_l: Tensor, ordering: str = "a"):

    idx = ravel_multi_index(idx_l, tt.shape)
    
    sorted_indices = torch.argsort(tt.ravel(), descending=ordering == "d")
   
    # Sorted indices for entire array
    sorted_indices = idx[sorted_indices]
    
    # Sorting indices
    idx_sort = unravel_index(sorted_indices, tt.shape)
    return idx_sort


# Fast-Marching-Method (FMM)
def FMM_tt_2D(tt, vv, dx, dz, status, trial_idx):
    """Function to perform fast-marching method in 2D"""
    nx, nz = vv.shape
    ns = np.array([nx, nz])
    dx_inv = 1.0 / dx
    dz_inv = 1.0 / dz
    ds_inv = np.array([dx_inv, dz_inv])
    # Various necessary variables
    drxns = [-1, 1]
    nbrs = np.zeros((4, 2), dtype=int)
    fdt = np.zeros(2)
    order = np.zeros(2, dtype=int)
    shift = np.zeros(2, dtype=int)
    shift_i = np.zeros(2, dtype=int)
    # FFM main loop
    while len(trial_idx) > 0:
        # Getting trial point with smallest traveltime
        active_idx = trial_idx.pop(0)
        status[active_idx[0], active_idx[1]] = 'k'
        
        # Creating indices of neighbouring points
        inbr = 0
        for iax in range(2):
            shift.fill(0)
            for idx in range(2):
                shift[iax] = drxns[idx]
                nbrs[inbr][:] = active_idx[:] + shift[:]
                inbr += 1
        
        # Update coefficients
        aa = np.zeros(2)
        bb = np.zeros(2)
        cc = np.zeros(2)
        # Loop over neighbouring points
        for idx, nb in enumerate(nbrs):
            nb = np.array(nb)
            # If point is outside the domain or has a known traveltime skip it
            if np.any(nb < 0) or np.any(nb >= ns) or status[nb[0], nb[1]] == 'k':
                continue
            # Checking if the velocity model is positive
            if vv[nb[0], nb[1]] > 0:
                fdt.fill(0.)
                order.fill(0)
                # Computing forward and backward derivatives from nb along each axis
                for iax in range(2):
                    shift.fill(0)
                    for ii in range(2):
                        shift_i.fill(0)
                        shift_i[iax] = drxns[ii]
                        nb_i = nb + shift_i
                        if (np.all(nb_i < ns) and np.all(np.zeros(2) <= nb_i)) and status[nb_i[0], nb_i[1]] == 'k':
                            order[ii] = 1
                            fdt[ii] = drxns[ii] * (tt[nb_i[0], nb_i[1]] - tt[nb[0], nb[1]]) * ds_inv[iax]
                        else:
                            order[ii] = 0
                            fdt[ii] = 0.0
                    # Selecting upwind derivative
                    if fdt[0] > -fdt[1]:
                        ii, shift[iax] = 0, -1
                    else:
                        ii, shift[iax] = 1, 1
                    # Selecting correct neighbouring point
                    nb_i = nb + shift
                    # Updating traveltime by solving quadratic equation
                    if order[ii] == 0:
                        aa[iax] = bb[iax] = cc[iax] = 0.0
                    else:
                        aa[iax] = ds_inv[iax] * ds_inv[iax]
                        bb[iax] = -2 * aa[iax] * tt[nb_i[0], nb_i[1]]
                        cc[iax] = tt[nb_i[0], nb_i[1]] * tt[nb_i[0], nb_i[1]] * aa[iax]
                # Point out of bounds
                a = np.sum(aa)
                if a == 0:
                    continue
                b = np.sum(bb)
                c = np.sum(cc) - 1 / (vv[nb[0], nb[1]] * vv[nb[0], nb[1]])
                det = b * b - 4.0 * a * c
                if det < 0.0:
                    # Negative determinant; set it to zero
                    new_t = - b / (2 * a)
                else:
                    new_t = (- b + np.sqrt(det)) / (2 * a)
                # Checking if new traveltime is smaller than current estimate for this point
                if new_t < tt[nb[0], nb[1]]:
                    tt[nb[0], nb[1]] = new_t
                    if status[nb[0], nb[1]] == 'u':
                        trial_idx.append(nb)
                        status[nb[0], nb[1]] = 't'
                    else:
                        trial_idx = sorting2D(tt, trial_idx)
    return


def FMM_tt_lin_fwd2D(delta_v, delta_tt, vv, tt, dx, dz):
    """Fast-marching method linearized forward"""
    nx = delta_v.shape[0]
    nz = delta_v.shape[1]
    ns = np.array([nx, nz])
    drxns = [-1, 1]
    dx_inv = 1.0 / dx
    dz_inv = 1.0 / dz
    ds_inv = np.array([dx_inv, dz_inv])
    
    # Shift variables
    order = np.zeros(2, dtype=int)
    shift = np.zeros(2, dtype=int)
    idrx = np.zeros(2, dtype=int)
    fdt0 = np.zeros(2)
    
    zz, xx = np.meshgrid(np.arange(nz), np.arange(nx))
    tt_idx = [[xx.flatten()[ii], zz.flatten()[ii]] for ii in range(zz.size)]
    # Sorting traveltime in ascending order
    tt_idx = sorting2D(tt, tt_idx)
    
    # Scaling the velocity perturbation
    delta_v_scaled = - 2.0 * delta_v / (vv * vv * vv)
    
    # Looping over all indices to solve linear equations from increasing traveltime values
    for idx_t0 in tt_idx:
        # If T = 0 or v = 0, then assuming zero to avoid singularity
        if tt[idx_t0[0], idx_t0[1]] == 0.0 or vv[idx_t0[0], idx_t0[1]] == 0.0:
            continue
        
        # Looping over
        fdt0.fill(0.0)
        idrx.fill(0)
        for iax in range(2):
            # Loop over neighbourning points to find up-wind direction
            fdt = np.zeros(2)
            order.fill(0)
            shift.fill(0)
            for idx in range(2):
                shift[iax] = drxns[idx]
                nb = idx_t0[:] + shift[:]
                # If point is outside the domain skip it
                if np.any(nb < 0) or np.any(nb >= ns):
                    continue
                if vv[nb[0], nb[1]] > 0.0:
                    order[idx] = 1
                    fdt[idx] = drxns[idx] * (tt[nb[0], nb[1]] - tt[idx_t0[0], idx_t0[1]]) * ds_inv[iax]
                else:
                    order[idx] = 0
            # Selecting upwind derivative
            shift.fill(0)
            if fdt[0] > -fdt[1] and order[0] > 0:
                idrx[iax], shift[iax] = -1, -1
            elif fdt[0] <= -fdt[1] and order[1] > 0:
                idrx[iax], shift[iax] = 1, 1
            else:
                idrx[iax] = 0
            nb = idx_t0[:] + shift[:]
            # Computing t0 space derivative
            fdt0[iax] = idrx[iax] * (tt[nb[0], nb[1]] - tt[idx_t0[0], idx_t0[1]]) * ds_inv[iax] * ds_inv[iax]
        # Using single stencil along z direction to update value
        if tt[idx_t0[0] + idrx[0], idx_t0[1]] > tt[idx_t0[0], idx_t0[1]]:
            denom = - 2.0 * idrx[1] * fdt0[1]
            if abs(denom) > 0.0:
                delta_tt[idx_t0[0], idx_t0[1]] += (- idrx[1] * 2.0 * fdt0[1] * delta_tt[
                    idx_t0[0], idx_t0[1] + idrx[1]] +
                                                   delta_v_scaled[idx_t0[0], idx_t0[1]]) / denom
        # Using single stencil along x direction to update value
        elif tt[idx_t0[0], idx_t0[1] + idrx[1]] > tt[idx_t0[0], idx_t0[1]]:
            denom = - 2.0 * idrx[0] * fdt0[0]
            if abs(denom) > 0.0:
                delta_tt[idx_t0[0], idx_t0[1]] += (- idrx[0] * 2.0 * fdt0[0] * delta_tt[
                    idx_t0[0] + idrx[0], idx_t0[1]] +
                                                   delta_v_scaled[idx_t0[0], idx_t0[1]]) / denom
        else:
            denom = - 2.0 * (idrx[0] * fdt0[0] + idrx[1] * fdt0[1])
            if abs(denom) > 0.0:
                delta_tt[idx_t0[0], idx_t0[1]] += (- idrx[0] * 2.0 * fdt0[0] * delta_tt[
                    idx_t0[0] + idrx[0], idx_t0[1]] +
                                                   - idrx[1] * 2.0 * fdt0[1] * delta_tt[
                                                       idx_t0[0], idx_t0[1] + idrx[1]] +
                                                   delta_v_scaled[idx_t0[0], idx_t0[1]]) / denom
    return


def select_upwind_der2D(tt, idx_t0, vv, ds_inv, iax):
    """Find upwind derivative along iax"""
    nx = vv.shape[0]
    nz = vv.shape[1]
    ns = np.array([nx, nz])
    nb = np.zeros(2, dtype=int)
    shift = np.zeros(2, dtype=int)
    drxns = [-1, 1]
    fdt = np.zeros(2)
    order = np.zeros(2, dtype=int)
    
    # Computing derivative for the neighboring points along iax
    for idx in range(2):
        shift[iax] = drxns[idx]
        nb[:] = idx_t0[:] + shift[:]
        # If point is outside the domain skip it
        if np.any(nb < 0) or np.any(nb >= ns):
            continue
        if vv[nb[0], nb[1]] > 0.0:
            order[idx] = 1
            fdt[idx] = drxns[idx] * (tt[nb[0], nb[1]] - tt[idx_t0[0], idx_t0[1]]) * ds_inv[iax]
        else:
            order[idx] = 0
    # Selecting upwind derivative
    if fdt[0] > -fdt[1] and order[0] > 0:
        fd, idrx = fdt[0], -1
    elif fdt[0] <= -fdt[1] and order[1] > 0:
        fd, idrx = fdt[1], 1
    else:
        fd, idrx = 0.0, 0
    return fd, idrx


def FMM_tt_lin_adj2D(delta_v, delta_tt, vv, tt, dx, dz):
    """Fast-marching method linearized forward"""
    nx = delta_v.shape[0]
    nz = delta_v.shape[1]
    ns = np.array([nx, nz])
    drxns = [-1, 1]
    dx_inv = 1.0 / dx
    dz_inv = 1.0 / dz
    ds_inv = np.array([dx_inv, dz_inv])
    
    # Internal variables
    order = np.zeros(2, dtype=int)
    shift = np.zeros(2, dtype=int)
    nbrs = np.zeros((4, 2), dtype=int)
    fdt_nb = np.zeros(4)
    order_nb = np.zeros(4, dtype=int)
    idrx_nb = np.zeros(4, dtype=int)
    
    zz, xx = np.meshgrid(np.arange(nz), np.arange(nx))
    tt_idx = [[xx.flatten()[ii], zz.flatten()[ii]] for ii in range(zz.size)]
    # Sorting traveltime in descending order
    tt_idx = sorting2D(tt, tt_idx, ordering="d")
    
    # Looping over all indices to solve linear equations from increasing traveltime values
    for idx_t0 in tt_idx:
        # If T = 0 or v = 0, then assuming zero to avoid singularity
        if tt[idx_t0[0], idx_t0[1]] == 0.0 or vv[idx_t0[0], idx_t0[1]] == 0.0:
            continue
        
        # Creating indices of neighbouring points
        # Order left/right bottom/top
        inbr = 0
        for iax in range(2):
            shift.fill(0)
            for idx in range(2):
                shift[iax] = drxns[idx]
                nbrs[inbr][:] = idx_t0[:] + shift[:]
                inbr += 1
        
        # Looping over neighbouring points
        fdt_nb.fill(0)
        idrx_nb.fill(0)
        for ib, nb in enumerate(nbrs):
            # Point outside of modeling domain
            if np.any(nb < 0) or np.any(nb >= ns):
                order_nb[ib] = 0
                continue
            # Point with lower traveltime compared to current point
            if tt[idx_t0[0], idx_t0[1]] > tt[nb[0], nb[1]]:
                order_nb[ib] = 0
                continue
            order_nb[ib] = 1
            # Getting derivative along given axis
            iax = 0 if ib in [0, 1] else 1
            fdt_nb[ib], idrx_nb[ib] = select_upwind_der2D(tt, nb, vv, ds_inv, iax)
            # Removing point if derivative at nb did not use idx_t0
            if ib in [0, 1]:
                # Checking x direction
                if idx_t0[0] != nb[0] + idrx_nb[ib]:
                    fdt_nb[ib], idrx_nb[ib] = 0.0, 0
            else:
                # Checking z direction
                if idx_t0[1] != nb[1] + idrx_nb[ib]:
                    fdt_nb[ib], idrx_nb[ib] = 0.0, 0
        
        # Updating delta_v according to stencil
        fdt_nb *= -idrx_nb
        fdt0 = 0.0
        fdt_nb[0] *= dx_inv
        fdt_nb[1] *= dx_inv
        fdt_nb[2] *= dz_inv
        fdt_nb[3] *= dz_inv
        
        if np.all(order_nb[:2]):
            fdt0, idrx0 = select_upwind_der2D(tt, idx_t0, vv, ds_inv, 1)
            fdt0 *= np.sign(idrx0) * dz_inv
        elif np.all(order_nb[2:]):
            fdt0, idrx0 = select_upwind_der2D(tt, idx_t0, vv, ds_inv, 0)
            fdt0 *= np.sign(idrx0) * dx_inv
        else:
            fdt0x, idrx0x = select_upwind_der2D(tt, idx_t0, vv, ds_inv, 0)
            fdt0z, idrx0z = select_upwind_der2D(tt, idx_t0, vv, ds_inv, 1)
            # Necessary to consider correct stencil central value
            if tt[idx_t0[0], idx_t0[1]] < tt[idx_t0[0] + idrx0x, idx_t0[1]]:
                fdt0x, idrx0x = 0.0, 0
            if tt[idx_t0[0], idx_t0[1]] < tt[idx_t0[0], idx_t0[1] + idrx0z]:
                fdt0z, idrx0z = 0.0, 0
            fdt0 = idrx0x * fdt0x * dx_inv + idrx0z * fdt0z * dz_inv
        
        # Update delta_v value
        delta_v[idx_t0[0], idx_t0[1]] -= (fdt_nb[0] * delta_v[idx_t0[0] - order_nb[0], idx_t0[1]]
                                          + fdt_nb[1] * delta_v[idx_t0[0] + order_nb[1], idx_t0[1]]
                                          + fdt_nb[2] * delta_v[idx_t0[0], idx_t0[1] - order_nb[2]]
                                          + fdt_nb[3] * delta_v[idx_t0[0], idx_t0[1] + order_nb[3]]
                                          - 0.5 * delta_tt[idx_t0[0], idx_t0[1]]) / fdt0
    
    # Scaling the velocity perturbation
    delta_v[:] = 2.0 * delta_v / (vv * vv * vv)
    
    return


class EikonalTT_2D(Operator):
    
    def __init__(self, vel, tt_data, dx, dz, SouPos, RecPos):
        """2D Eikonal-equation traveltime prediction operator"""
        # Setting Domain and Range of the operator
        super(EikonalTT_2D, self).__init__(vel, tt_data)
        # Setting acquisition geometry
        self.nSou = SouPos.shape[0]
        self.nRec = RecPos.shape[0]
        self.SouPos = SouPos.copy()
        self.RecPos = RecPos.copy()
        dataShape = tt_data.shape
        if dataShape[0] != self.nSou:
            raise ValueError("Number of sources inconsistent with traveltime vector (shape[0])")
        if dataShape[1] != self.nRec:
            raise ValueError("Number of receivers inconsistent with traveltime vector (shape[1])")
        self.dx = dx
        self.dz = dz
        self.nx = vel.shape[0]
        self.nz = vel.shape[1]
    
    def forward(self, add, model, data):
        """Forward non-linear traveltime prediction"""
        self.checkDomainRange(model, data)
        if not add:
            data.zero()
        dataNd = data.getNdArray()
        velNd = model.getNdArray()
        # Initialization
        tt = np.zeros((self.nx, self.nz))
        for iShot in range(self.nSou):
            # Initial conditions
            status = np.reshape(np.array(["u"] * nx * nz), (nx, nz))  # All points are unknown
            tt.fill(np.inf)
            trial_idx = []
            # Initial conditions
            idx = self.SouPos[iShot, 0]
            idz = self.SouPos[iShot, 1]
            tt[idx, idz] = 0.0
            status[idx, idz] = 't'  # Trial status
            trial_idx.append([idx, idz])
            # Sorting trial time ascending order
            trial_idx = sorting2D(tt, trial_idx)
            FMM_tt_2D(tt, velNd, self.dx, self.dz, status, trial_idx)
            for iRec in range(self.nRec):
                dataNd[iShot, iRec] += tt[self.RecPos[iRec, 0], self.RecPos[iRec, 1]]
        return


class EikonalTT_lin_2D(Operator):
    
    def __init__(self, vel, tt_data, dx, dz, SouPos, RecPos):
        """2D Eikonal-equation traveltime prediction operator"""
        # Setting Domain and Range of the operator
        super(EikonalTT_lin_2D, self).__init__(vel, tt_data)
        # Setting acquisition geometry
        self.nSou = SouPos.shape[0]
        self.nRec = RecPos.shape[0]
        self.SouPos = SouPos.copy()
        self.RecPos = RecPos.copy()
        dataShape = tt_data.shape
        if dataShape[0] != self.nSou:
            raise ValueError("Number of sources inconsistent with traveltime vector (shape[0])")
        if dataShape[1] != self.nRec:
            raise ValueError("Number of receivers inconsistent with traveltime vector (shape[1])")
        self.dx = dx
        self.dz = dz
        self.nx = vel.shape[0]
        self.nz = vel.shape[1]
        # Background model
        self.vel = vel.clone()
        self.vel.copy(vel)
    
    def forward(self, add, model, data):
        """Forward linearized traveltime prediction"""
        self.checkDomainRange(model, data)
        if not add:
            data.zero()
        dataNd = data.getNdArray()
        modelNd = model.getNdArray()
        vel0Nd = self.vel.getNdArray()
        # Initialization
        tt0 = np.zeros((self.nx, self.nz))
        for iShot in range(self.nSou):
            ###################################
            # Computing background traveltime #
            ###################################
            # Initial conditions
            status = np.reshape(np.array(["u"] * nx * nz), (nx, nz))  # All points are unknown
            tt0.fill(np.inf)
            trial_idx = []
            # Initial conditions
            idx = self.SouPos[iShot, 0]
            idz = self.SouPos[iShot, 1]
            tt0[idx, idz] = 0.0
            status[idx, idz] = 't'  # Trial status
            trial_idx.append([idx, idz])
            # Sorting trial time ascending order
            trial_idx = sorting2D(tt0, trial_idx)
            FMM_tt_2D(tt0, vel0Nd, self.dx, self.dz, status, trial_idx)
            ###################################
            # Computing linearized traveltime #
            ###################################
            delta_tt = np.zeros((self.nx, self.nz))
            FMM_tt_lin_fwd2D(modelNd, delta_tt, vel0Nd, tt0, self.dx, self.dz)
            for iRec in range(self.nRec):
                dataNd[iShot, iRec] += delta_tt[self.RecPos[iRec, 0], self.RecPos[iRec, 1]]
        return
    
    def adjoint(self, add, model, data):
        """Adjoint linearized traveltime prediction"""
        self.checkDomainRange(model, data)
        if not add:
            model.zero()
        dataNd = data.getNdArray()
        modelNd = model.getNdArray()
        vel0Nd = self.vel.getNdArray()
        # Initialization
        tt0 = np.zeros((self.nx, self.nz))
        for iShot in range(self.nSou):
            ###################################
            # Computing background traveltime #
            ###################################
            # Initial conditions
            status = np.reshape(np.array(["u"] * nx * nz), (nx, nz))  # All points are unknown
            tt0.fill(np.inf)
            trial_idx = []
            # Initial conditions
            idx = self.SouPos[iShot, 0]
            idz = self.SouPos[iShot, 1]
            tt0[idx, idz] = 0.0
            status[idx, idz] = 't'  # Trial status
            trial_idx.append([idx, idz])
            # Sorting trial time ascending order
            trial_idx = sorting2D(tt0, trial_idx)
            FMM_tt_2D(tt0, vel0Nd, self.dx, self.dz, status, trial_idx)
            ###################################
            # Computing velocity perturbation #
            ###################################
            delta_tt = np.zeros((self.nx, self.nz))
            delta_v = np.zeros((self.nx, self.nz))
            # Injecting traveltime to correct grid positions
            for iRec in range(self.nRec):
                delta_tt[self.RecPos[iRec, 0], self.RecPos[iRec, 1]] = dataNd[iShot, iRec]
            FMM_tt_lin_adj2D(delta_v, delta_tt, vel0Nd, tt0, self.dx, self.dz)
            modelNd[:] += delta_v
        return
    
    def set_vel(self, vel):
        """Function to set background velocity model"""
        self.vel.copy(vel)


if __name__ == "__main__":
    import occamypy
    # Plotting
    import matplotlib
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    
    # %matplotlib inline
    params = {
        'figure.figsize'     : (12, 5),
        'image.interpolation': 'nearest',
        'image.cmap'         : 'gray',
        'savefig.dpi'        : 300,  # to adjust notebook inline plot size
        'axes.labelsize'     : 18,  # fontsize for x and y labels (was 10)
        'axes.titlesize'     : 18,
        'font.size'          : 18,
        'legend.fontsize'    : 18,
        'xtick.labelsize'    : 18,
        'ytick.labelsize'    : 18,
        'text.usetex'        : False
    }
    matplotlib.rcParams.update(params)
    
    # Fast-Marching-Method (FMM)
    dx = dz = 0.1
    nx, nz = 201, 101
    x = np.arange(nx) * dx
    z = np.arange(nz) * dz
    # Background Velocity model
    vv0 = np.zeros((nx, nz))
    vv0[:, :] = 1.0 + z * 0.1
    vv0 = occamypy.VectorNumpy(vv0)
    # Gaussian anomaly
    zz, xx = np.meshgrid(z, x)
    dst = np.sqrt(xx ** 2 + zz ** 2)
    sigma = 1.0
    xloc = 101 * dx
    zloc = 51 * dz
    gauss = np.exp(-(((xx - xloc) ** 2 + (zz - zloc) ** 2) / (2.0 * sigma ** 2)))
    # True model
    vv = vv0.clone()
    vv[:] -= gauss * 0.5
    
    plt.figure()
    plt.imshow(vv.plot().T, extent=[x[0], x[-1], z[-1], z[0]],
               cmap=plt.get_cmap("jet_r"), aspect=0.5)
    plt.grid(True)
    plt.xlabel("x [km]")
    plt.ylabel("z [km]")
    plt.title("True model")
    plt.colorbar(orientation="horizontal", label='Velocity [km/s]', aspect=50)
    plt.tight_layout(pad=.5)
    plt.show()
    
    # Source/Receiver positions: 6 sources, 201 receivers
    src_pos = np.array([[ix, nz - 1] for ix in np.arange(0, nx, 40)])
    rec_pos = np.array([[ix, 0] for ix in np.arange(0, nx)])
    # Instantiating non-linear operator
    Eik2D_Op = EikonalTT_2D(velocity=vv, sampling=(dx, dz), sources=src_pos, receivers=rec_pos)
    Eik2D_Lin_Op = EikonalTT_lin_2D(velocity=vv, sampling=(dx, dz), sources=src_pos, receivers=rec_pos)
    Eik2D_NlOp = occamypy.NonlinearOperator(Eik2D_Op, Eik2D_Lin_Op, Eik2D_Lin_Op.set_vel)
    
    # Creating observed data
    tt_data = Eik2D_Op * vv
    
    # Plotting traveltime vector
    fig, ax = plt.subplots()
    for src in range(len(src_pos)):
        ax.plot(rec_pos[:, 0] * dx, tt_data.plot()[src], lw=4)
        ax.scatter(src_pos[src, 0] * dx, 6, marker="x", label=f"source {src}")
    ax.grid()
    plt.xlabel("x [km]")
    plt.ylabel("Traveltime [s]")
    plt.ylim([5.0, 15.0])
    plt.legend()
    plt.title("Acquired Data")
    ax.autoscale(enable=True, axis='x', tight=True)
    ax.invert_yaxis()
    plt.show()
    
    minBound = vv.clone().set(1.0)  # min velocity
    maxBound = vv.clone().set(2.5)  # max velocity
    BFGSBsolver = occamypy.LBFGSB(occamypy.BasicStopper(niter=500, tolg_proj=1e-32), m_steps=30)
    
    # Creating problem object using Smoothing filter and Gradient mask
    grad_smoothing = occamypy.ConvND(vv0, occamypy.VectorNumpy((10, 10)).set(1.))
    mask = vv.clone().zero()
    mask[int(nx * 0.1):int(nx * 0.9), int(nz * 0.1):int(nz * 0.9)] = 1.0
    mask = grad_smoothing * mask
    
    Smoothing = occamypy.ConvND(vv0, occamypy.VectorNumpy((2, 2)).set(1.))
    Eik2D_Inv_NlOp = occamypy.NonlinearOperator(Eik2D_Op, Eik2D_Lin_Op * Smoothing, Eik2D_Lin_Op.set_vel)
    L2_tt_prob = occamypy.NonlinearLeastSquares(vv0.clone(), tt_data, Eik2D_Inv_NlOp,
                                                minBound=minBound, maxBound=maxBound, grad_mask=mask)
    
    BFGSBsolver.run(L2_tt_prob, verbose=True)
    
    fig, ax = plt.subplots(figsize=(20, 10))
    im = ax.imshow(vv0.plot().T, extent=[x[0], x[-1], z[-1], z[0]],
                   cmap=plt.get_cmap("jet_r"), aspect=0.5)
    ax = plt.gca()
    ax.grid()
    plt.xlabel("x [km]")
    plt.ylabel("z [km]")
    plt.title("Initial model")
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("bottom", size="5%", pad=-1.2)
    cbar = plt.colorbar(im, orientation="horizontal", cax=cax)
    cbar.set_label('Velocity [km/s]')
    plt.show()
    
    fig, ax = plt.subplots(figsize=(20, 10))
    im = ax.imshow(L2_tt_prob.model.plot().T, extent=[x[0], x[-1], z[-1], z[0]],
                   cmap=plt.get_cmap("jet_r"), aspect=0.5)
    ax = plt.gca()
    ax.grid()
    plt.xlabel("x [km]")
    plt.ylabel("z [km]")
    plt.title("Inverted model")
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("bottom", size="5%", pad=-1.2)
    cbar = plt.colorbar(im, orientation="horizontal", cax=cax)
    cbar.set_label('Velocity [km/s]')
    plt.show()
