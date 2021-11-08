#!/home/shatira/miniconda3/bin/python
import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import plotly.express as px
from itertools import zip_longest
import csv
from collections import Counter
import os
import argparse
def readfiles(files, outdir="methrandir_output", prefix="methrandir", coverage=4, method="weighted_average"):
    if not os.path.exists(outdir) and outdir != "":
        os.mkdir(outdir)
    units = pd.read_csv(files, sep='\t', header=0)
    combined = units['group']+'_'+units['replicate'].astype(str)
    design = units['group']
    mapdesign = list(Counter(design).values())

    with open(os.path.join(outdir, f"{prefix}.filtered_methylation.csv"), 'w', newline="") as all:
        wr = csv.writer(all, quoting=csv.QUOTE_MINIMAL)
        if method == "weighted_average":
            wr.writerow((["chr", "position"] + list(dict.fromkeys(design))))
        elif method == "raw":
            wr.writerow(["chr", "position"] + list(combined.values))
        fileList = units.loc[:, "path"].values
        files = [open(filename) for filename in fileList]
        for lines in zip_longest(*files, fillvalue=''):
            keep = []
            meths = []
            unmeths = []
            broken = False
            # attempt to filter
            for line in lines:
                meth = int(line.split('\t')[3])
                unmeth = int(line.split('\t')[4])
                if meth + unmeth < coverage:
                    broken = True
                    break
                else:
                    meths.append(meth)
                    unmeths.append(unmeth)
                    keep.append(meth/sum([meth, unmeth]))
            if broken:
                pass
            else:
                weighted_avg = []
                grouped = []
                groupcov = []
                counter = 0
                cov = list(zip(meths, unmeths))
                cov = [sum(x) for x in cov]
                if method == "weighted_average":
                    for l in mapdesign:
                        grouped.append(keep[counter:l+counter])
                        groupcov.append(cov[counter:l+counter])
                        counter += l
                    for i in range(len(mapdesign)):
                        weighted_avg.append(np.average(
                            grouped[i], weights=groupcov[i]))
                    wr.writerow(lines[1].split('\t')[0:2] + weighted_avg)
                elif method == "raw":
                    wr.writerow(lines[1].split('\t')[0:2] + keep)
        for fh in files:
            fh.close()


def compute_pca(file, outdir="methrandir_output", prefix="methrandir"):
    all = pd.read_csv(file, sep=",", header=0)
    df = all.iloc[:, 2:].T
    index = all.iloc[:, 2:].columns
    pca = PCA(n_components=3)
    components = pca.fit_transform(df)
    total_var = pca.explained_variance_ratio_.sum() * 100
    p = pca.explained_variance_ratio_
    fig = px.scatter_3d(
        components, x=0, y=1, z=2, color=index,
        title=f'Total Explained Variance: {total_var:.2f}%',
        labels={'0': f'PC 1 : {p[0]*100:.2f}%',
                '1': f'PC 2 : {p[1]*100:.2f}%', '2': f'PC 3 : {p[2]*100:.2f}%'}
    )
    fig.write_image(os.path.join(outdir, f"{prefix}.3DPCA.png"))
    fig.write_html(os.path.join(outdir, f"{prefix}.3DPCA.HTML"))

    fig = px.scatter(components, x=0, y=1, color=index,
                     labels={'0': f'PC 1 : {p[0]*100:.2f}%',
                             '1': f'PC 2 : {p[1]*100:.2f}%'})
    fig.write_image(os.path.join(outdir, f"{prefix}.2DPCA.png"))
    fig.write_html(os.path.join(outdir, f"{prefix}.2DPCA.HTML"))


def main():
    parser = argparse.ArgumentParser(description='Methylation Data Overview Utility')
    parser.add_argument(
        "-f", "--files", help="tab seperated file containing paths of sorted bismark CX reports and their",required=True)
    parser.add_argument(
        "-o", "--out_prefix", help="output files prefix", default="methrandir")
    parser.add_argument(
        "-outdir", "--outdir", help="output directory", default="methrandir_output")
    parser.add_argument(
        "-m", "--method", help="model biological replicates", default="weighted_average")
    parser.add_argument(
        "-c", "--min_coverage", type=int, help="minimum number of reads for each position on all samples", default=4)

    args = parser.parse_args()

    readfiles(files=args.files, outdir=args.outdir,
              prefix=args.out_prefix, coverage=args.min_coverage, method=args.method)

    compute_pca(file=os.path.join(
        args.outdir, f"{args.out_prefix}.filtered_methylation.csv"), outdir=args.outdir, prefix=args.out_prefix)    

if __name__ == "__main__":
    main()
    
