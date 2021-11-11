import argparse
import sys

from . import xyz_py


def struct_info_func(args):
    """
    Wrapper for cli call to get_ bonds, dihedrals and angles

    Parameters
    ----------
        args : argparser object
            command line arguments

    Returns
    -------
        None

    """

    labels, coords = xyz_py.load_xyz(args.xyz_file)

    labels = xyz_py.remove_numbers(labels)
    labels = xyz_py.add_numbers(labels)

    f_head = args.xyz_file.split(".")[0]

    # Custom cutoffs
    if len(args.adjust_cutoff) % 2:
        sys.exit("Error: Too few cutoffs provided")

    for it in range(1, len(args.adjust_cutoff), 2):
        args.adjust_cutoff[it] = float(args.adjust_cutoff[it])

    cutoff_dict = {}
    for it in range(1, len(args.adjust_cutoff), 2):
        cutoff_dict[args.adjust_cutoff[it-1]] = args.adjust_cutoff[it]

    # Generate neighbourlist
    neigh_list = xyz_py.get_neighborlist(
        labels,
        coords,
        adjust_cutoff=cutoff_dict
    )

    # Get structural data
    xyz_py.get_bonds(
        labels,
        coords,
        save=True,
        f_name="{}_bonds.dat".format(f_head),
        style="labels",
        neigh_list=neigh_list
    )
    xyz_py.get_angles(
        labels,
        coords,
        save=True,
        f_name="{}_angles.dat".format(f_head),
        style="labels",
        neigh_list=neigh_list
    )
    xyz_py.get_dihedrals(
        labels,
        coords,
        save=True,
        f_name="{}_dihedrals.dat".format(f_head),
        style="labels",
        neigh_list=neigh_list
    )

    return


def read_args(arg_list=None):
    """
    Parser for command line arguments. Uses subparsers for individual programs

    Parameters
    ----------
        args : argparser object
            command line arguments

    Returns
    -------
        None

    """

    description = '''
    A package for manipulating xyz files and chemical structures
    '''

    epilog = '''
    To display options for a specific program, use xyz_py PROGRAMNAME -h
    '''

    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='prog')

    # Generate Input files

    struct_info = subparsers.add_parser(
        'struct_info',
        description="Extracts structural information (bonds, angles and \
                     dihedrals) from xyz file"
    )
    struct_info.set_defaults(func=struct_info_func)

    struct_info.add_argument(
        'xyz_file',
        type=str,
        help='File containing xyz coordinates in .xyz format'
    )

    struct_info.add_argument(
        "--adjust_cutoff",
        type=str,
        nargs='+',
        default=[],
        metavar=["symbol", "cutoff"],
        help="Change cutoff for symbol to cutoff e.g. Gd 2.5"
    )
    struct_info.add_argument(
        "--save_style",
        type=str,
        default="indices",
        choices=["labels", "indices"],
        help="Save bonds, angles, and dihedrals as atom labels or \
                atom indices"
    )

    # If arg_list==None, i.e. normal cli usage, parse_args() reads from
    # "sys.argv". The arg_list can be used to call the argparser from the
    # back end.

    # read sub-parser
    parser.set_defaults(func=lambda args: parser.print_help())
    args = parser.parse_args(arg_list)
    args.func(args)


def main():
    read_args()
