import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import regex as re
import scipy.stats


class InvalidTypeCol(Exception):
    pass


def compute_df_cat(df, col, target_col, ordered_xticks):
    df = df[[col, target_col]].reset_index()
    df[col].fillna('NULL', inplace=True)

    # convert to float to match type in reindexing if 'col' column is float, otherwise reindexing
    # is failing leading to nan values inserted instead of correct values
    if isinstance(df.loc[0][col], float):
        ordered_xticks = list([float(x) for x in ordered_xticks])

    group_df = df.groupby(col)[target_col].agg(['mean', 'count', 'std'])
    ix = pd.Index(ordered_xticks, name=col)
    group_df = group_df.reindex(ix).reset_index()  # name='counts_total'

    return group_df


def get_confidence(n, std, confidence_level=0.95):
    quantile = (1 + confidence_level) / 2
    inv_norm_dist = scipy.stats.norm.ppf(quantile)
    frac = (inv_norm_dist * std) / np.sqrt(n)
    # bounds = {'sup': (y - frac) * 100, 'inf': (y + frac) * 100}
    # disabled code, meant to be used if sup & low bound are not the same, but be careful, return type
    # will differ and use of this function was not planned to use this result, require to change "errorbar" parameters
    return frac


# Wrapper to apply get_confidence easily on whole dataframe
def wrapper_confidence(row, confidence_level):
    return get_confidence(row['count'], row['std'], confidence_level)


def compute_df_num(df, col, target_col, q, bins=None, ordered_classes=None):
    df = df[[col, target_col]].reset_index()
    df[col] = pd.to_numeric(df[col])

    isNULL = sum(df[col].isnull()) > 0

    df2 = pd.DataFrame()
    # if some null values, will treat null and non null values separately
    if isNULL:
        df2 = df.loc[df[col].isnull(), :].copy()
        df2[col].fillna('NULL', inplace=True)
        df = df.loc[~df[col].isnull(), :].copy()

    # cut col in bins
    if bins is not None:
        binning = pd.cut(df[col], bins=bins, precision=2)
    else:
        binning = pd.qcut(df[col], q=q, precision=2, duplicates='drop')
        bin_count = binning.value_counts()

        # if only one bin, take thinner quantiles until more than one bin
        if len(bin_count) < 2:
            i = 0
            while len(bin_count) < 2:
                i += 1
                binning = pd.qcut(df[col], q=q * 2 ** i, precision=2, duplicates='drop')
                bin_count = binning.value_counts()

    df_binning = pd.DataFrame({col: binning, target_col: df[target_col].values}).reset_index()
    df_binning[col] = df_binning[col].astype(str)

    group_df = df_binning.groupby(col)[target_col].agg(['mean', 'count', 'std']).reset_index()
    # reorder the bins in increasing order and put the NULL first if exists
    group_df["start_bin"] = pd.to_numeric(group_df[col].map(lambda x: re.search(r'[+-]?(\d*[.])?\d+', x[1:])[0]))
    group_df.sort_values("start_bin", inplace=True)
    group_df.drop("start_bin", axis=1, inplace=True)

    if isNULL:
        group_df2 = df2.groupby(col)[target_col].agg(['mean', 'count', 'std']).reset_index()
        group_df = pd.concat([group_df, group_df2], axis=0)

    return group_df


def scale(original, loc_scale, multiplier=0.5):
    return original + ((loc_scale - 1) * original) * multiplier


def plot_regression(df,
                    title,
                    col,
                    target_col,
                    annot=True,
                    plot_confidence=True,
                    annot_confidence=False,
                    ordered_xticks=None,
                    x_label="",
                    y_label_left="N. observations per modality",
                    y_label_right='Mean of the target ',
                    rotation=0,
                    xticks_font_size=18,
                    annot_font_size=14,
                    type_col="cat",
                    confidence_level=0.95,
                    size=1,
                    x_warp=1,
                    y_warp=1):

    # change size of graph based on size
    figsize = (20 * x_warp, 10 * y_warp)
    figsize = tuple([size * x for x in figsize])

    # hacky way to change font size to comply with graph size
    xticks_font_size = scale(xticks_font_size, size)
    annot_font_size = scale(annot_font_size, size)

    # check if col has no 0 variance
    assert len(df[col].value_counts()) > 1, "One unique value in " + col

    if ordered_xticks is None:
        if type_col == "num_discrete":
            ordered_xticks = [str(x) for x in list(pd.to_numeric(df[col]).sort_values().drop_duplicates())]
        else:
            ordered_xticks = list(df[col].drop_duplicates())

        # remove None and insert NULL at first position if needed
        if None in ordered_xticks:
            ordered_xticks.remove(None)
            ordered_xticks.insert(0, "NULL")

    # df_res = pd.DataFrame()

    # build the data to plot
    if type_col == "cat":
        df_res = compute_df_cat(df=df, col=col, target_col=target_col,
                                ordered_xticks=ordered_xticks)

    elif type_col == "num":
        df_res = compute_df_num(df=df, col=col, target_col=target_col, q=10)

    elif type_col == "num_discrete":
        if isinstance(df[col][0], str):
            raise InvalidTypeCol("Type of col parameter is not numerical, use 'cat' for non numerical data")
        df_res = compute_df_cat(df=df, col=col, target_col=target_col,
                                ordered_xticks=ordered_xticks)

    else:
        raise InvalidTypeCol("You entered an invalid type_col parameter, valids ones are: 'cat', 'num', 'num_discrete'")

    fontsize = 18
    title_fontsize = 24

    fig, ax1 = plt.subplots(figsize=figsize)
    plt.xticks(rotation=rotation, fontsize=xticks_font_size)
    plt.title(title, fontsize=title_fontsize)

    # first axes : bar plot of the distribution of col
    color_bar = 'tab:orange'

    ind = np.arange(len(df_res))
    ax1.bar(ind, df_res["count"].values, width=0.9, color=color_bar)

    ax1.set_xlabel(x_label, fontsize=fontsize)
    ax1.set_ylabel(y_label_left, color=color_bar, fontsize=fontsize)
    ax1.tick_params(axis='y', labelcolor=color_bar, labelsize=fontsize)
    ax1.set_xticks(ind)
    ax1.set_xticklabels(list(df_res[col]))

    # second axes : representation of the target
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color_mean = 'tab:blue'
    ax2.set_ylabel(y_label_right, fontsize=fontsize, color=color_mean)  # we already handled the x-label with ax1

    # plot the confidence bars
    if plot_confidence:
        array_confidence = df_res.apply(wrapper_confidence, confidence_level=confidence_level, axis=1)
        ax2.errorbar(ind, df_res['mean'], array_confidence, linestyle='None', marker='',
                     ecolor=color_mean, capsize=scale(8, size), markeredgewidth=scale(2, size))
        points_val = list(zip(ind, df_res['mean'], array_confidence))

        # annotate the points with confidence value
        if annot_confidence:
            for cur in points_val:
                ax2.annotate(
                    str(round(cur[1] + cur[2], 2)),
                    xy=(cur[0], cur[1]),
                    xycoords='data',
                    textcoords='offset pixels',
                    xytext=(0, scale(30, size, 0.6)),
                    fontsize=annot_font_size * 0.9
                )

    ax2.plot(ind, list(df_res['mean']), color=color_mean, marker='o', label="nada", lw=3)

    ax2.tick_params(axis='y', labelsize=fontsize, labelcolor=color_mean)
    ax2.set_ylim(bottom=0, top=max(df_res['mean']) * 1.1)

    # add point annotations
    if annot:
        # indm = [item for item in list(range(len(df_count_total))) for i in range(len(df_res)//len(df_count_total))]
        for x, y in zip(ind, df_res['mean'].values):
            ax2.annotate(
                str(round(y, 1)), xy=(x, y),
                xytext=(x, y + max(df_res['mean']) * 0.02),
                fontsize=annot_font_size
            )

    plt.show()
    return None
