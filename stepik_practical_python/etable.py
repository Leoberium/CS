import zipfile
import pandas as pd


def task1(wb):
    sheet_names = wb.sheet_names()
    sh = wb.sheet_by_name(sheet_names[0])
    n_min = sh.row_values(6)[2]
    for row_num in range(7, 27):
        temp = sh.row_values(row_num)
        n_min = min(n_min, temp[2])
    print(n_min)


def task2():
    df = pd.read_excel("salaries.xlsx", index_col=0)
    print(df.median(axis=1).idxmax())
    print(df.mean(axis=0).idxmax())


def task3():
    df = pd.read_excel("trekking1.xlsx")
    df.columns = ["Название"] + list(df.columns[1:])
    df_sorted = df.sort_values(by=[df.columns[1], df.columns[0]], ascending=[False, True])
    print("\n".join(df_sorted["Название"]))


def task4():
    df2 = pd.read_excel("trekking2.xlsx", sheet_name=1, index_col=0)
    # df2 = df2[~df2.index.duplicated(keep="first")]
    df1 = pd.read_excel("trekking2.xlsx", sheet_name=0, index_col=0).fillna(0)
    dfm = df2.join(df1)
    print(dfm.apply(lambda x: x.iloc[0] * x.iloc[1:] / 100.0, axis=1).sum().astype("int"))


def task5():
    df2 = pd.read_excel("trekking3.xlsx", sheet_name=1, index_col=1)
    df1 = pd.read_excel("trekking3.xlsx", sheet_name=0, index_col=0).fillna(0)
    dfm = df2.join(df1)

    def f(grp):
        return pd.Series({
            "cal": (grp.iloc[:, 1] * grp.iloc[:, 2] / 100.0).sum(),
            "prot": (grp.iloc[:, 1] * grp.iloc[:, 3] / 100.0).sum(),
            "fat": (grp.iloc[:, 1] * grp.iloc[:, 4] / 100.0).sum(),
            "carb": (grp.iloc[:, 1] * grp.iloc[:, 5] / 100.0).sum()
        })

    grouped = dfm.groupby("День").apply(f).astype("int")
    for t in grouped.itertuples():
        print(" ".join(map(str, t[1:])))


def task6():
    data = []
    with zipfile.ZipFile("rogaikopyta.zip") as z:
        for file in z.namelist():
            with z.open(file, "r") as t:
                df = pd.read_excel(t, skiprows=1, header=None)
                name, s = df.iloc[0, 1], int(df.iloc[0, 3])
                data.append((name, s))
    data.sort()
    data = [" ".join(map(str, t)) + "\n" for t in data]
    with open("answer.txt", "w") as o:
        o.writelines(data)


if __name__ == '__main__':
    task6()
