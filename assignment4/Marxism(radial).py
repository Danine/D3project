from pyecharts import options as opts
from pyecharts.charts import Tree

def tree_base() -> Tree:
    data = [
        {
            "children":[
                {"name":"导论"},
                {"name":"世界的物质性及发展规律"},
                {"name":"实践与认识及其发展规律"},
                {"name":"人类社会及其发展规律"},
                {"name":"资本主义的本质及规律"},
                {"name":"资本主义的发展及其趋势"},
                {"name":"社会主义的发展及其规律"},
                {"name":"共产主义崇高理想及其最终实现"},
                {"name":"后记"},
            ],
            "name":"马克思主义基本原理概论"}
    ]

    c = (
        Tree(init_opts=opts.InitOpts(width = "900px",height = "900px"))
        .add("", data, collapse_interval=3, layout="radial", symbol="emptyCircle", itemstyle_opts=opts.ItemStyleOpts(border_color="rgb(12, 12, 150)"))
        .set_global_opts(title_opts = opts.TitleOpts(title="Radial Tree Layout"))
    )
    return c

c = tree_base()
c.render()