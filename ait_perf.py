#!/usr/bin/python3
#coding=utf-8


'''
ait性能测试
'''

import os

def exec_jmx(file):
    print("*"*30)
    print(file)


    # 执行测试
    os.system("{0} {1} {2} {3} {4}".format(
        r"d:\apache-jmeter-5.0\bin\jmeter",
        "-n -t",
        file + ".jmx",
        "-l",
        file + ".jtl"
    ))

    target_path = r"{0}\{1}".format(r"d:\wangbin\my_workspace\Jmeter_prj\ait_perf\report",
                                    file.rpartition('\\')[2])

    if os.path.exists(target_path):
        os.system("rd /s /q {0}".format(target_path))
    os.system("mkdir {0}".format(target_path))

    # 导出报告
    os.system("{0} {1} {2} {3} {4}".format(
        r"d:\apache-jmeter-5.0\bin\jmeter",
        "-g",
        file + ".jtl",
        "-o",
        target_path
    ))




def ait_hdbfcs_sjpt_jgs():
    '''
    设计配套-结构树-对配套结构进行全部展开
    :return:
    '''
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sjpt_jgs_10")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sjpt_jgs_50")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sjpt_jgs_100")
    # exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sjpt_jgs_300")

def ait_hdbfcs_sjztpt_jgs():
    '''
    设计状态配置-结构树-对配套结构进行全部展开
    '''
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sjztpt_jgs_10")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sjztpt_jgs_50")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sjztpt_jgs_100")
    # exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sjztpt_jgs_300")

def ait_hdbfcs_sszt_jgs():
    '''
    实施状态-结构树-对配套结构进行全部展开
    :return:
    '''
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_jgs_10")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_jgs_50")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_jgs_100")
    # exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_jgs_300")

def ait_hdbfcs_sszt_sb():
    '''
    实施状态-设备-对配套结构进行全部展开
    :return:
    '''
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_sb_10")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_sb_50")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_sb_100")
    # exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_sb_300")

def ait_hdbfcs_sszt_dljq():
    '''
    实施状态-电连接器-对配套结构进行全部展开
    :return:
    '''
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_dljq_10")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_dljq_50")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_dljq_100")
    # exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_dljq_300")

def ait_hdbfcs_sszt_dl():
    '''
    实施状态-电缆-对配套结构进行全部展开
    :return:
    '''
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_dl_10")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_dl_50")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_dl_100")
    # exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sszt_dl_300")


def ait_hdbfcs_jx_yclb():
    '''
    基线-右侧列表-展示配套产品信息列表
    :return:
    '''
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_jx_yclb_10")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_jx_yclb_50")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_jx_yclb_100")
    # exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_jx_yclb_300")

def ait_hdbfcs_ztjjqrd_yclb():
    '''
    状态交接确认单-右侧列表	-展示配套产品信息列表
    :return:
    '''
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_ztjjqrd_yclb_10")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_ztjjqrd_yclb_50")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_ztjjqrd_yclb_100")
    # exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_ztjjqrd_yclb_300")

def ait_hdbfcs_sjpt_yclb():
    '''
    设计配套-右侧列表-创建单个配套产品
    :return:
    '''
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sjpt_yclb_10")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sjpt_yclb_50")
    exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sjpt_yclb_100")
    # exec_jmx(r"D:\wangbin\my_workspace\Jmeter_prj\ait_perf\ait_hdbfcs_sjpt_yclb_300")


if __name__=="__main__":
    # ait_hdbfcs_sjpt_jgs()
    ait_hdbfcs_sjztpt_jgs()
    # ait_hdbfcs_sszt_jgs()
    #
    # ait_hdbfcs_sszt_sb()
    # ait_hdbfcs_sszt_dl()
    # ait_hdbfcs_sszt_dljq()
    #
    # ait_hdbfcs_jx_yclb()
    # ait_hdbfcs_ztjjqrd_yclb()
    # ait_hdbfcs_sjpt_yclb()







