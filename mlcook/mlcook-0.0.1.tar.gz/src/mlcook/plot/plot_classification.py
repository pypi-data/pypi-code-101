import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import regex as re
import scipy.stats
import sys


class InvalidTypeCol(Exception):
    pass


def compute_df_cat(df, col, target_col, ordered_classes, ordered_xticks):
    df = df[[col, target_col]].reset_index()
    df[col].fillna('NULL', inplace=True)

    #convert to float to match type in reindexing if 'col' column is float, otherwise reindexing
    #is failing leading to nan values inserted instead of correct values
    if isinstance(df.loc[0][col], float):
        ordered_xticks =  list([float(x) for x in ordered_xticks])

    group = df.groupby([col, target_col]).size()
    df_group = group.unstack(target_col).fillna(0).stack()

    multi_ix = pd.MultiIndex.from_product([ordered_xticks, ordered_classes], names=[col, target_col])

    df_group = df_group.reindex(multi_ix).reset_index(name='counts_group')#multi_ix

    df_total = df.groupby([col]).size()
    ix = pd.Index(ordered_xticks, name=col)
    df_total = df_total.reindex(ix).reset_index(name='counts_total')#ix

    df_res = pd.merge(df_group, df_total, how='left', on=col)
    df_res['pct'] = df_res['counts_group'] / df_res['counts_total'] * 100

    return df_res


def get_confidence(count_total, local_proba, threshold=5):
    n = count_total
    y = local_proba/100
    percent = (100 - threshold/2)/100
    inv_norm_dist = scipy.stats.norm.ppf(percent)
    frac = (inv_norm_dist * np.sqrt(y * (1-y)))/np.sqrt(n)
    # bounds = {'sup': (y - frac) * 100, 'inf': (y + frac) * 100}
    # disabled code, meant to be used if sup & low bound are not the same, but be careful, return type
    # will differ and use of this function was not planned to use this result, require to change "errorbar" parameters
    frac = frac * 100
    return frac


# Wrapper to apply get_confidence easily on whole dataframe
def wrapper_confidence(row, threshold):
    return get_confidence(row.counts_total, row.pct, threshold)


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
                binning = pd.qcut(df[col], q=q * 2**i, precision=2, duplicates='drop')
                bin_count = binning.value_counts()

    df_binning = pd.DataFrame({col: binning, target_col: df[target_col].values}).reset_index()
    df_binning[col] = df_binning[col].astype(str)

    group = df_binning.groupby([col, target_col]).size()
    df_group = group.unstack(target_col).fillna(0).stack()
    df_group = df_group.reset_index(name='counts_group')

    df_total = df_binning.groupby([col]).size()
    df_total = df_total.reset_index(name='counts_total')

    df_res = pd.merge(df_group, df_total, how='left', on=col)
    df_res['pct'] = df_res['counts_group'] / df_res['counts_total'] * 100

    # reorder the bins in increasing order and put the NULL first if exists
    df_res["start_bin"] = pd.to_numeric(df_res[col].map(lambda x: re.search(r'[+-]?(\d*[.])?\d+', x[1:])[0]))
    df_res.sort_values("start_bin", inplace=True)
    df_res.drop("start_bin", axis=1, inplace=True)

    if isNULL:
        df2_res = df2.groupby([col, target_col]).size()
        multi_ix = pd.MultiIndex.from_product([["NULL"], ordered_classes], names=[col, target_col])
        df2_res = df2_res.reindex(multi_ix).reset_index(name='counts_group')
        df2_res["counts_group"].fillna(0, inplace=True)
        df2_res["counts_total"] = df2_res["counts_group"].sum()
        df2_res['pct'] = df2_res['counts_group'] / df2_res['counts_total'] * 100

        # concatenate the NULL part and the non NULL part
        df_res = pd.concat([df2_res, df_res], axis=0)

    return df_res


def scale(original, loc_scale, multiplier=0.5):
    return original + ((loc_scale - 1) * original) * multiplier


def plot_classification(df,
                        title,
                        col,
                        target_col,
                        plot_confidence=True,
                        annot_confidence=True,
                        annot=True,
                        ordered_classes=None,
                        ordered_xticks=None,
                        x_label="",
                        y_label_left="Nb d'observations par tranche",
                        y_label_right='Pct de souscription par tranche',
                        rotation=0,
                        xticks_font_size=18,
                        annot_font_size=14,
                        unit='%',
                        legend_loc='upper right',
                        legend_size=18,
                        type_col="cat",
                        confidence_threshold=5,
                        size=1,
                        x_warp=1,
                        y_warp=1):

    # change size of graph based on size
    figsize = (20 * x_warp, 10 * y_warp)
    figsize = tuple([size * x for x in figsize])

    # hacky way to change font size to comply with graph size
    xticks_font_size = scale(xticks_font_size, size)
    annot_font_size = scale(annot_font_size, size)
    legend_size = scale(legend_size, size)

    # check if col has no 0 variance
    assert len(df[col].value_counts()) > 1, "One unique value in " + col

    if ordered_classes is None:
        ordered_classes = list(df[target_col].drop_duplicates())

    if ordered_xticks is None:
        if type_col == "num_discrete":
            ordered_xticks = [str(x) for x in list(pd.to_numeric(df[col]).sort_values().drop_duplicates())]
        else:
            ordered_xticks = list(df[col].drop_duplicates())

        # remove None and insert NULL at first position if needed
        if None in ordered_xticks:
            ordered_xticks.remove(None)
            ordered_xticks.insert(0, "NULL")

    df_res = pd.DataFrame()

    # build the data to plot
    if type_col == "cat":
        df_res = compute_df_cat(df=df, col=col, target_col=target_col,
                                ordered_classes=ordered_classes, ordered_xticks=ordered_xticks)

    elif type_col == "num":
        df_res = compute_df_num(df=df, col=col, target_col=target_col, q=10, ordered_classes=ordered_classes)

    elif type_col == "num_discrete":
        if isinstance(df[col][0], str):
            raise InvalidTypeCol("Type of col parameter is not numerical, use 'cat' for non numerical data")
        df_res = compute_df_cat(df=df, col=col, target_col=target_col,
                                ordered_classes=ordered_classes, ordered_xticks=ordered_xticks)

    else:
        raise InvalidTypeCol("You entered an invalid type_col parameter, valids ones are: 'cat', 'num', 'num_discrete'")

    fontsize = 18
    title_fontsize = 24

    fig, ax1 = plt.subplots(figsize=figsize)
    plt.xticks(rotation=rotation, fontsize=xticks_font_size)
    plt.title(title, fontsize=title_fontsize)

    # first axes : bar plot of the distribution of col
    color_bar = 'tab:orange'
    try:
        df_count_total = df_res[[col, "counts_total"]].copy()
    except Exception as loc_err:
        print("'counts_total' or '{}' column may be not found, maybe df_res is still empty due to type col not being filled ?".format(col),
              file=sys.stderr)
        raise loc_err

    df_count_total.drop_duplicates(inplace=True)
    ind = np.arange(len(df_count_total))
    ax1.bar(ind, df_count_total["counts_total"].values, width=0.9, color=color_bar)

    ax1.set_xlabel(x_label, fontsize=fontsize)
    ax1.set_ylabel(y_label_left, color=color_bar, fontsize=fontsize)
    ax1.tick_params(axis='y', labelcolor=color_bar, labelsize=fontsize)
    ax1.set_xticks(ind)
    ax1.set_xticklabels(list(df_count_total[col]))

    # second axes : representation of the target
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel(y_label_right, fontsize=fontsize)  # we already handled the x-label with ax1

    list_color = ['tab:blue', 'tab:green', 'tab:red', 'tab:purple',
                  'tab:brown',
                  'tab:pink',
                  'tab:gray',
                  'tab:olive',
                  'tab:cyan']

    # plot the confidence bars
    points_val = []
    if plot_confidence:
        classes = list(set(df_res[target_col].values))
        for index, classe in enumerate(classes):
            cur = df_res.loc[df_res[target_col] == classe]
            array_confidence = cur.apply(wrapper_confidence, threshold=confidence_threshold, axis=1)
            ax2.errorbar(ind, cur['pct'], array_confidence, linestyle='None', marker='',
                         ecolor=list_color[index], capsize=scale(8, size), markeredgewidth=scale(2, size))
            points_val.append(list(zip(ind, cur['pct'], array_confidence)))

    # annotate the points with confidence value
    if annot_confidence:
        for el in points_val:
            for cur in el:
                ax2.annotate(
                    str(round(cur[2], 2)),
                    xy=(cur[0], cur[1]),
                    xycoords='data',
                    textcoords='offset pixels',
                    xytext=(0, scale(30, size, 0.6)),
                    fontsize=annot_font_size * 0.9
                )

    for i, cl in enumerate(ordered_classes):
        df_class = df_res.loc[df_res[target_col].values == cl, [col, "pct"]].copy()
        ax2.plot(ind, list(df_class['pct']), color=list_color[i], marker='o', label="nada", lw=3)


    ax2.tick_params(axis='y', labelsize=fontsize)
    ax2.set_ylim(bottom=0, top=max(df_res['pct']) * 1.1)

    # add point annotations
    if annot:
        indm = [item for item in list(range(len(df_count_total))) for i in range(len(df_res)//len(df_count_total))]
        for x, y in zip(indm, df_res['pct'].values):
            if unit == '%':
                ax2.annotate(
                    str(round(y, 2))+unit, xy=(x, y),
                    xytext=(x, y + max(df_res['pct']) * 0.02),
                    fontsize=annot_font_size
                )
            else:
                ax2.annotate(
                    str(round(y, 1))+unit, xy=(x, y),
                    xytext=(x, y + max(df_res['pct']) * 0.02),
                    fontsize=annot_font_size
                )

    # add legend
    handles, _ = ax2.get_legend_handles_labels()
    ax2.legend(handles=handles,
               labels=ordered_classes,
               loc=legend_loc,
               fontsize=legend_size,
               framealpha=0.5)

    plt.show()
    return None
