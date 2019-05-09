from pyecharts import options as opts
from pyecharts.charts import Tree

def tree_base() -> Tree:
    data = [
        {
            "children": [
                {
                    "children":[
                        {"name":"c_cpp_properties.json"}
                    ],
                    "name":".vscode"
                },
                {
                    "children":[
                        {"name": "apps"},
                        {"name": "LenovoDrivers"},
                        {
                            "children": [
                                {"name": "AppleApplicationSupport64.msi"},
                                {"name": "AppleApplicationSupport64.msi.log"},
                                {"name": "AppleMobileDeviceSupport6464.msi"},
                                {"name": "AppleMobileDeviceSupport6464.msi.log"},
                            ],
                            "name":"win7_x64"
                        }
                    ],
                    "name": "downloads",
                },
                {
                    "children": [
                        {
                            "children": [
                                {
                                    "children":[
                                        {
                                            "children":[
                                                {"name":"PROSETDX"},
                                                {"name":"SETUP"},
                                                {"name":"SNMP"},
                                            ],
                                            "name":"APPS"
                                        },
                                        {
                                            "children":[
                                                {"name":"Winx64"},
                                            ],
                                            "name":"PRO1000"
                                        },
                                        {"name":"verfile.tic"},
                                    ],
                                    "name": "ETHERNET"
                                }, 
                                {
                                    "children":[
                                        {
                                            "children":[
                                                {"name":"intel_sidebar_lefttoright.bmp"},
                                                {"name":"license.txt"}
                                            ],
                                            "name":"data"
                                        },
                                        {
                                            "children":[
                                                {"name":"DpinstWaterMark.bmp"},
                                                {"name":"DpinstWaterMark_right.bmp"}
                                            ],
                                            "name":"dpinstWaterMark"
                                        },
                                        {
                                            "children":[
                                                {
                                                    "children":[
                                                        {"name":"370810225019140f00.bseq"},
                                                        {"name":"ibtproppage.dll"},
                                                        {"name":"ibtsiva.exe"},
                                                        {"name":"ibtusb.cat"},
                                                        {"name":"ibtusb.inf"},
                                                        {"name":"ibtusb.sys"},
                                                    ],
                                                    "name":"SDP"},
                                                {"name":"SFP"},
                                                {"name":"STP"},
                                                {"name":"WP"},
                                                {"name":"WSP"}
                                            ],
                                            "name":"ibtusb"
                                        },
                                        {"name":"dpinst.exe"},
                                        {"name":"dpinst.xml"},
                                    ],
                                    "name": "IntelBT"},
                                {"name": "OSD"},
                                {
                                    "children":[
                                        {"name":"dpinst.exe"},
                                        {"name":"Eula0c0aESP.tx_"},
                                        {"name":"InstNT.exe"},
                                        {"name":"LenovoShortcut"},
                                    ],
                                    "name": "UNAV"},
                                {
                                    "chlidren":[
                                        {
                                            "children":[
                                                {
                                                    "children":[
                                                        {"name":"DPInst64.exe"},
                                                        {"name":"iprodifx.exe"},
                                                        {"name":"netwbw02.cat"},
                                                        {"name":"NETwew01.sys"},
                                                        {"name":"Netwtw02.INF"},
                                                    ],
                                                    "name":"WinT"}
                                            ],
                                            "name":"Drivers"},
                                        {
                                            "children":[
                                                {
                                                    "children":[
                                                        {"name":"Driver.msi"},
                                                        {"name":"PROSetEnterprise.msi"},
                                                        {"name":"WiFi.msi"},
                                                    ],
                                                    "name":"data"},
                                                {"name":"Setup.exe"},
                                                {"name":"setup.xml"},
                                            ],
                                            "name":"Install"}
                                    ],
                                    "name": "WLANINT"},
                                ],
                            "name": "WIN"},
                    ],
                    "name": "DRIVERS"
                },
                {"name":"FFOutput"},
                {
                    "children":[
                        {"name":"ExtremeGraphics"},
                        {"name":"gp"},
                        {
                            "children":[
                                {"name":"IntelCpHDCPSvc.log"},
                                {"name":"IntelCPHS.log"},
                                {"name":"IntelGFX.log"},
                                {"name":"IntelGFXCoin.log"},
                            ],
                            "name":"Logs"},
                        {
                            "children":[
                                {"name":"Data"},
                                {"name":"WUSetupLauncher.exe"},
                            ],
                            "name":"Wireless"},
                    ],
                    "name":"Intel"},
                {"name":"LenovoDrivers"},
                {"name":"MSOCache"},
                {"name":"MyDrivers"},
                {"name":"PerfLogs"},
                {
                    "children":[
                        {
                            "children":[
                                {
                                    "children":[
                                        {"name":"af.txt"},
                                        {"name":"an.txt"},
                                        {"name":"eo.txt"},
                                        {"name":"tt.txt"},
                                        {"name":"zh-cn.txt"},
                                    ],
                                    "name":"Lang"},
                                {"name":"7z.dll"},
                                {"name":"7zFM.exe"},
                                {"name":"Uninstall.exe"},
                            ],
                            "name":"7-Zip"},
                        {
                            "children":[
                                {
                                    "children":[
                                        {"name":"AME-Version.txt"},
                                        {"name":"Dolby-Version.txt"},
                                        {"name":"PCI-Version.txt"},
                                    ],
                                    "name":"Adobe Media Encoder CS6"},
                                {
                                    "children":[
                                        {"name":"amtlib.dll.DEL"},
                                        {"name":"painter.ini"},
                                    ],
                                    "name":"Adobe Photoshop CC 2018"}
                            ],
                            "name":"Adobe"},
                        {"name":"Git"},
                        {
                            "children":[
                                {"name":"HAXM"},
                                {"name":"iCLS Client"},
                                {"name":"IntelSGXPSW"},
                                {"name":"WiFi"},
                                {"name":"WiFiDrivers"},
                                {"name":"Wired Networking"},
                            ],
                            "name":"Intel"},
                        {"name":"mingw-w64"},
                        {
                            "children":[
                                {"name":"DLLs"},
                                {"name":"Doc"},
                                {"name":"include"},
                                {"name":"LICENSE.txt"},
                                {"name":"python.exe"},
                                {"name":"vcruntime140.dll"},
                            ],
                            "name":"Python36"},
                        {
                            "children":[
                                {"name":"TpShocks"},
                            ],
                            "name":"ThinkPad"},
                        {"name":"UNP"},
                    ],
                    "name":"Program Files"
                },
                {"name":"Program Files (x86)"},
                {
                    "children":[
                        {"name":"Adobe"},
                        {"name":"Apple"},
                        {"name":"Comms"},
                        {"name":"DG"},
                        {"name":"Dolby"},
                        {"name":"Git"},
                        {"name":"Lenovo"},
                        {"name":"McAfee"},
                        {"name":"MySQL"},
                    ],
                    "name":"ProgramData"},
                {"name":"RmDownloads"},
                {
                    "children":[
                        {"name":"appcache"},
                        {"name":"Backups"},
                        {"name":"bin"},
                        {"name":"config"},
                        {"name":"drivers"},
                        {"name":"dumps"},
                    ],
                    "name":"Steam"},
                {"name":"aow_drv.log"},
                {"name":"d2f42068.ini"},
            ],
            "name": "本地磁盘:C",}
    ]

    c = (
        Tree(init_opts=opts.InitOpts(width = "900px", height = "900px", page_title="filePath"))
        .add("", data, collapse_interval=3, layout="radial", symbol="emptyCircle", itemstyle_opts=opts.ItemStyleOpts(border_color="rgb(12, 12, 150)"))
        .set_global_opts(title_opts = opts.TitleOpts(title="本地磁盘C的文件路径"))
    )
    return c

c = tree_base()
c.render()