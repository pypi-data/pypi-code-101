#!/usr/bin/env python3

from astropy.io import fits
from astropy.wcs import WCS
from reproject import reproject_from_healpix, reproject_to_healpix
import argparse


def cli():
    # Help string to be shown using the -h option
    descStr = """
    Regrid a HEALPIX FITS file to target FITS image.
    A simple implementation of Astropy and Reproject FITS handling.
    This script reprojects a HEALPIX projected FITS file to an image projection.
    Beware of any projection issues this may cause!

    """

    # Parse the command line options
    parser = argparse.ArgumentParser(
        description=descStr, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "fitsHEAL", metavar="HEALPIX.fits", nargs=1, help="FITS map in HEALPIX format."
    )
    parser.add_argument(
        "template",
        metavar="template.fits",
        nargs=1,
        help="Template FITS map to project onto.",
    )
    parser.add_argument(
        "out", metavar="output.fits", nargs=1, help="FITS map to save output to."
    )
    parser.add_argument(
        "-e",
        dest="Extension",
        default=1,
        help="Extension to select from HEALPIX file. Default 1.",
    )
    parser.add_argument(
        "-f", dest="field", default=0, help="Select field within extension. Default 0."
    )
    parser.add_argument(
        "-c",
        dest="COORDSYS",
        default="galactic",
        help="Specify COORDSYS card. Default 'galactic'.",
    )
    args = parser.parse_args()

    main(
        outf=args.fitsHEAL[0],
        inf=args.template[0],
        outf1=args.out[0],
        ext=args.Extension,
        field=args.field,
        coordsys=args.COORDSYS,
    )


def main(outf: str, inf: str, outf1: str, ext: int, field: int, coordsys: str) -> None:
    """Main script.

    Args:
        outf (str): Healpix file
        inf (str): Target file
        outf1 (str): Output file
        ext (int): Healpix extension
        field (int): Column from healpix file.
        coordsys (str): Coordsys to use.
    """    
    # Read in the HEALPIX file
    print("Reading files...")
    # Read in HEALPIX file
    hdu2 = fits.open(outf)[int(ext)]

    # Read in target fits file
    hdu1 = fits.open(inf)[0]

    print("Generating header...")
    target_wcs = WCS(hdu1)
    target_header = target_wcs.celestial.to_header()
    hdu2.header["COORDSYS"] = coordsys
    # Regrid
    print("Regridding...")
    array, footprint = reproject_from_healpix(hdu2, target_header, field=int(field), shape_out=target_wcs.celestial.array_shape)

    # Save the file!
    print("Saving output to " + outf1)
    hdu = fits.PrimaryHDU(array, header=target_header)
    hdul = fits.HDUList([hdu])
    hdul.writeto(outf1, overwrite=True)


if __name__ == "__main__":
    cli()
