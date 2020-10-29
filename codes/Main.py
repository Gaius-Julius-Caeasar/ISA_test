# coding=utf-8
# 编译日期：2020-10-29 14:32:23
# 版权所有：www.i-search.com.cn
import ubpa.init_input as iinput
from ubpa.base_util import StdOutHook, ExceptionHandler
import ubpa.iimg as iimg
import ubpa.ikeyboard as ikeyboard
import ubpa.itools.rpa_fun as rpa_fun
import ubpa.iexcel as iexcel
import ubpa.itools.rpa_str as rpa_str
import time
import pdb
from ubpa.ilog import ILog
from ubpa.base_img import set_img_res_path
import getopt
from sys import argv
import sys
import os

class NewProject1:
     
    def __init__(self,**kwargs):
        self.__logger = ILog(__file__)
        self.path = set_img_res_path(__file__)
        self.robot_no = ''
        self.proc_no = ''
        self.job_no = ''
        self.input_arg = ''
        if('robot_no' in kwargs.keys()):
            self.robot_no = kwargs['robot_no']
        if('proc_no' in kwargs.keys()):
            self.proc_no = kwargs['proc_no']
        if('job_no' in kwargs.keys()):
            self.job_no = kwargs['job_no']
        ILog.JOB_NO, ILog.OLD_STDOUT = self.job_no, sys.stdout
        sys.stdout = StdOutHook(self.job_no, sys.stdout)
        ExceptionHandler.JOB_NO, ExceptionHandler.OLD_STDERR = self.job_no, sys.stderr
        sys.excepthook = ExceptionHandler.handle_exception
        if('input_arg' in kwargs.keys()):
            self.input_arg = kwargs['input_arg']
            if(len(self.input_arg) <= 0):
                self.input_arg = iinput.load_init(__file__)
            if self.input_arg is None:
                sys.exit(0)
      
    def flow1(self):
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:2020102811431669279,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',offsetX=100,times=2,image=r'snapshot_20201029102745076.png',image_size=r'107X19',win_title=r'银行日记账-条件查询',continue_on_error='break',img_res_path = self.path)
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:2020102811443953682,Title:模拟按键,Note:')
        time.sleep(0.3)
        ikeyboard.key_send_cs(waitfor=10.000,text='2016')
        time.sleep(0.3)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:20201029104525554947,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',offsetX=240,times=2,image=r'snapshot_20201029102745076.png',image_size=r'107X19',win_title=r'银行日记账-条件查询',continue_on_error='break',img_res_path = self.path)
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:20201029104628537954,Title:模拟按键,Note:')
        ikeyboard.key_send_cs(waitfor=10.000,text=11)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:20201029103034188926,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',offsetX=100,times=2,image=r'snapshot_20201029103053436.png',image_size=r'94X18',win_title=r'银行日记账-条件查询',continue_on_error='break',img_res_path = self.path)
        time.sleep(0.3)
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:20201029102936035924,Title:模拟按键,Note:')
        time.sleep(0.3)
        ikeyboard.key_send_cs(waitfor=10.000,text='2017')
        time.sleep(0.3)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:20201029104712257957,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',offsetX=240,times=2,image=r'snapshot_20201029103053436.png',image_size=r'94X18',win_title=r'银行日记账-条件查询',continue_on_error='break',img_res_path = self.path)
        time.sleep(0.3)
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:20201029104741631965,Title:模拟按键,Note:')
        ikeyboard.key_send_cs(waitfor=10.000,text='11')
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:2020102811454933884,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20201028114606050.png',image_size=r'79X24',win_title=r'银行日记账-条件查询',continue_on_error='break',img_res_path = self.path)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:20201028133001493128,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20201028133026462.png',image_size=r'73X91',win_title=r'金蝶EAS-IT_Test',continue_on_error='break',img_res_path = self.path)
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:20201028133117833130,Title:模拟按键,Note:')
        ikeyboard.key_send_cs(waitfor=10.000,text='1102{Enter}{Enter}')
        #图片检测
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:20201029092629318884,Title:图片检测,Note:')
        tvar_20201029092629318885=iimg.img_exists(waitfor=30.000,win_title=r'金蝶EAS-IT_Test',image=r'snapshot_20201029092535882.png',img_res_path = self.path)
        print('[flow1] [图片检测] [20201029092629318884]  返回值：[' + str(type(tvar_20201029092629318885)) + ']' + str(tvar_20201029092629318885))
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:2020102813020652490,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20201029091730871.png',image_size=r'79X23',win_title=r'金蝶EAS-IT_Test',continue_on_error='break',img_res_path = self.path)
      
    def flow2(self,fangshi=None,leixing=None,initial=4,num=0,excel=0):
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201029100501969918,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',offsetX=10,image=r'snapshot_20201029100607886.png',image_size=r'14X24',win_title=r'金蝶EAS-IT_Test',continue_on_error='break',img_res_path = self.path)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201029100714286921,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20201029100801595.png',image_size=r'85X22',win_title=r'金蝶EAS-IT_Test',continue_on_error='break',img_res_path = self.path)
        #工作表行数获取
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028230910820504,Title:工作表行数获取,Note:')
        excel=iexcel.get_rows_count(path='C:/Users/Administrator/Desktop/银行日记账20201020112540会计录入收款信息.xlsx')
        print('[flow2] [工作表行数获取] [20201028230910820504]  返回值：[' + str(type(excel)) + ']' + str(excel))
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028143452321202,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20201028143508572.png',image_size=r'77X29',win_title=r'金蝶EAS-IT_Test',continue_on_error='break',img_res_path = self.path)
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201029015023339827,Title:模拟按键,Note:')
        ikeyboard.key_send_cs(waitfor=10.000,text='{Tab}')
        # For循环
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:flow2,StepNodeTag:20201028230954859509,Title:For循环,Note:')
        for num in range(excel-3):
            #单元格读取
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201029012445614787,Title:单元格读取,Note:')
            time.sleep(0.3)
            tvar_20201029012445614788=iexcel.read_cell(path='C:/Users/Administrator/Desktop/银行日记账20201020112540会计录入收款信息.xlsx',cell='B'+str(initial),cell_type='time')
            print('[flow2] [单元格读取] [20201029012445614787]  返回值：[' + str(type(tvar_20201029012445614788)) + ']' + str(tvar_20201029012445614788))
            time.sleep(0.3)
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028143734693212,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text=tvar_20201029012445614788)
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028150809975282,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text='{Tab}')
            #单元格读取
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028144321938225,Title:单元格读取,Note:')
            time.sleep(0.3)
            tvar_20201028144321939226=iexcel.read_cell(path='C:/Users/Administrator/Desktop/银行日记账20201020112540会计录入收款信息.xlsx',cell='C'+str(initial),cell_type='time')
            print('[flow2] [单元格读取] [20201028144321938225]  返回值：[' + str(type(tvar_20201028144321939226)) + ']' + str(tvar_20201028144321939226))
            time.sleep(0.3)
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028144335510228,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text=tvar_20201028144321939226)
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028144459937234,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text='{Tab}')
            #单元格读取
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028144459937236,Title:单元格读取,Note:')
            time.sleep(0.3)
            tvar_20201028144459937237=iexcel.read_cell(path='C:/Users/Administrator/Desktop/银行日记账20201020112540会计录入收款信息.xlsx',cell='I'+str(initial),cell_type='string')
            print('[flow2] [单元格读取] [20201028144459937236]  返回值：[' + str(type(tvar_20201028144459937237)) + ']' + str(tvar_20201028144459937237))
            time.sleep(0.3)
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028144459937235,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text=tvar_20201028144459937237)
            time.sleep(0.5)
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028151111503295,Title:模拟按键,Note:')
            time.sleep(0.5)
            ikeyboard.key_send_cs(waitfor=10.000,text='{Tab}')
            #单元格读取
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:202010291412063991055,Title:单元格读取,Note:')
            time.sleep(0.3)
            leixing=iexcel.read_cell(path='C:/Users/Administrator/Desktop/银行日记账20201020112540会计录入收款信息.xlsx',cell='D'+str(initial),cell_type='string')
            print('[flow2] [单元格读取] [202010291412063991055]  返回值：[' + str(type(leixing)) + ']' + str(leixing))
            time.sleep(0.3)
            # IF分支
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:flow2,StepNodeTag:202010291416021701074,Title:IF分支,Note:')
            if leixing == '银收':
                #模拟按键
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:202010291416444871078,Title:模拟按键,Note:')
                ikeyboard.key_send_cs(waitfor=10.000,text='{Down 15}')
            elif leixing == '银付':
                #模拟按键
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:202010291417369811080,Title:模拟按键,Note:')
                ikeyboard.key_send_cs(waitfor=10.000,text='{Down 8}')
            else:
                pass
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028153949690307,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text='{Enter}')
            #单元格读取
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028154040326309,Title:单元格读取,Note:')
            time.sleep(0.3)
            tvar_20201028154040327310=iexcel.read_cell(path='C:/Users/Administrator/Desktop/银行日记账20201020112540会计录入收款信息.xlsx',cell='E'+str(initial),cell_type=None)
            print('[flow2] [单元格读取] [20201028154040326309]  返回值：[' + str(type(tvar_20201028154040327310)) + ']' + str(tvar_20201028154040327310))
            time.sleep(0.3)
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028154124182312,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text=tvar_20201028154040327310)
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028173223637496,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text='{Tab 4}')
            #单元格读取
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:202010291422234261086,Title:单元格读取,Note:')
            time.sleep(0.3)
            fangshi=iexcel.read_cell(path='C:/Users/Administrator/Desktop/银行日记账20201020112540会计录入收款信息.xlsx',cell='J'+str(initial),cell_type='string')
            print('[flow2] [单元格读取] [202010291422234261086]  返回值：[' + str(type(fangshi)) + ']' + str(fangshi))
            time.sleep(0.3)
            # IF分支
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:flow2,StepNodeTag:202010291423319511100,Title:IF分支,Note:')
            if fangshi =='电汇':
                #模拟按键
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:202010291426471281103,Title:模拟按键,Note:')
                ikeyboard.key_send_cs(waitfor=10.000,text='{Down 8}')
            elif fangshi =='银行承兑汇票（收）':
                #模拟按键
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:202010291427017501104,Title:模拟按键,Note:')
                ikeyboard.key_send_cs(waitfor=10.000,text='{Down 3}')
            elif fangshi =='转帐':
                #模拟按键
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:202010291427022791107,Title:模拟按键,Note:')
                ikeyboard.key_send_cs(waitfor=10.000,text='{Down 17}')
            else:
                pass
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028154301537329,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text='{Enter}')
            #单元格读取
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028154445770331,Title:单元格读取,Note:')
            time.sleep(0.3)
            tvar_20201028154445771332=iexcel.read_cell(path='C:/Users/Administrator/Desktop/银行日记账20201020112540会计录入收款信息.xlsx',cell='K'+str(initial),cell_type='string')
            print('[flow2] [单元格读取] [20201028154445770331]  返回值：[' + str(type(tvar_20201028154445771332)) + ']' + str(tvar_20201028154445771332))
            time.sleep(0.3)
            #replace
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028165150667415,Title:replace,Note:')
            tvar_20201028165150667416=rpa_str.replace(string=tvar_20201028154445771332,old='#',new='{#}')
            print('[flow2] [replace] [20201028165150667415]  返回值：[' + str(type(tvar_20201028165150667416)) + ']' + str(tvar_20201028165150667416))
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028165226010429,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text=tvar_20201028165150667416)
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028154630210337,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text='{Tab}')
            #单元格读取
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028154707544339,Title:单元格读取,Note:')
            time.sleep(0.3)
            tvar_20201028154707545340=iexcel.read_cell(path='C:/Users/Administrator/Desktop/银行日记账20201020112540会计录入收款信息.xlsx',cell='L'+str(initial),cell_type=None)
            print('[flow2] [单元格读取] [20201028154707544339]  返回值：[' + str(type(tvar_20201028154707545340)) + ']' + str(tvar_20201028154707545340))
            time.sleep(0.3)
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028154718140342,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text=tvar_20201028154707545340)
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028154748193347,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text='{Tab}')
            #单元格读取
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028154805912349,Title:单元格读取,Note:')
            time.sleep(0.3)
            tvar_20201028154805912350=iexcel.read_cell(path='C:/Users/Administrator/Desktop/银行日记账20201020112540会计录入收款信息.xlsx',cell='M'+str(initial),cell_type=None)
            print('[flow2] [单元格读取] [20201028154805912349]  返回值：[' + str(type(tvar_20201028154805912350)) + ']' + str(tvar_20201028154805912350))
            time.sleep(0.3)
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028154840804352,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text=tvar_20201028154805912350)
            #模拟按键
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201028172525264494,Title:模拟按键,Note:')
            ikeyboard.key_send_cs(waitfor=10.000,text='{Tab 4}')
            #相加
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201029015908212843,Title:相加,Note:')
            initial=rpa_fun.add(a=initial,b=1)
            print('[flow2] [相加] [20201029015908212843]  返回值：[' + str(type(initial)) + ']' + str(initial))
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow2,StepNodeTag:20201029100341149915,Title:模拟按键,Note:')
        ikeyboard.key_send_cs(waitfor=10.000)
      
    def leixing(self):
        pass
      
    def login(self):
        #热键输入
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:login,StepNodeTag:2020102716440633945,Title:热键输入,Note:')
        ikeyboard.key_send_cs(waitfor=10.000,text=r'#d')
        #鼠标双击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:login,StepNodeTag:2020102716440633944,Title:鼠标双击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',times=2,image=r'snapshot_20201029103253721.png',image_size=r'38X29',img_res_path = self.path)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:login,StepNodeTag:2020102716440633942,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20201027163736752.png',image_size=r'272X15',win_title=r'金蝶EAS系统登录',continue_on_error='break',img_res_path = self.path)
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:login,StepNodeTag:2020102716440633941,Title:模拟按键,Note:')
        ikeyboard.key_send_cs(waitfor=10.000,text="123456")
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:login,StepNodeTag:2020102716440633943,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20201027164204785.png',image_size=r'76X18',win_title=r'金蝶EAS系统登录',continue_on_error='break',img_res_path = self.path)
      
    def Main(self):
        #子流程
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:2020102716441979756,Title:子流程,Note:')
        tvar20201027164419797561=self.login()
        print('[Main] [子流程] [2020102716441979756]  返回值：[' + str(type(tvar20201027164419797561)) + ']' + str(tvar20201027164419797561))
        # Try异常
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:Main,StepNodeTag:2020102813042663292,Title:Try异常,Note:')
        try:
            #图片检测
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:2020102813045662794,Title:图片检测,Note:')
            tvar_2020102813045662895=iimg.img_exists(waitfor=30.000,win_title=r'账号重复登录',image=r'snapshot_20201028130520424.png',img_res_path = self.path)
            print('[Main] [图片检测] [2020102813045662794]  返回值：[' + str(type(tvar_2020102813045662895)) + ']' + str(tvar_2020102813045662895))
            #鼠标点击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:2020102813052718697,Title:鼠标点击,Note:')
            iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20201028130553617.png',image_size=r'80X21',win_title=r'账号重复登录',continue_on_error='break',img_res_path = self.path)
        except Exception as e:
            pass
        finally:
            #鼠标点击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:2020102716442586158,Title:鼠标点击,Note:')
            time.sleep(5)
            iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20201029105623930.png',image_size=r'82X13',win_title=r'金蝶EAS-IT_Test',continue_on_error='break',img_res_path = self.path)
            #鼠标点击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:2020102716463348960,Title:鼠标点击,Note:')
            iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20201027164652739.png',image_size=r'151X20',win_title=r'金蝶EAS-IT_Test',continue_on_error='break',img_res_path = self.path)
            #鼠标点击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:2020102716465797562,Title:鼠标点击,Note:')
            iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20201027164724771.png',image_size=r'223X28',win_title=r'金蝶EAS-IT_Test',continue_on_error='break',img_res_path = self.path)
            #鼠标双击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:2020102716515656866,Title:鼠标双击,Note:')
            iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',times=2,image=r'snapshot_20201027165408189.png',image_size=r'212X21',win_title=r'金蝶EAS-IT_Test',img_res_path = self.path)
            #子流程
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:2020102811290944859,Title:子流程,Note:')
            tvar20201028112909448591=self.flow1()
            print('[Main] [子流程] [2020102811290944859]  返回值：[' + str(type(tvar20201028112909448591)) + ']' + str(tvar20201028112909448591))
            #图片检测
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20201029092656397894,Title:图片检测,Note:')
            tvar_20201029092656397895=iimg.img_exists(waitfor=30.000,win_title=r'金蝶EAS-IT_Test',image=r'snapshot_20201029092735462.png',img_res_path = self.path)
            print('[Main] [图片检测] [20201029092656397894]  返回值：[' + str(type(tvar_20201029092656397895)) + ']' + str(tvar_20201029092656397895))
            #子流程
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20201028173523203502,Title:子流程,Note:')
            tvar202010281735232035021=self.flow2()
            print('[Main] [子流程] [20201028173523203502]  返回值：[' + str(type(tvar202010281735232035021)) + ']' + str(tvar202010281735232035021))
 
if __name__ == '__main__':
    ILog.begin_init()
    robot_no = ''
    proc_no = ''
    job_no = ''
    input_arg = ''
    try:
        argv = sys.argv[1:]
        opts, args = getopt.getopt(argv,"hr:p:j:i:",["robot = ","proc = ","job = ","input = "])
    except getopt.GetoptError:
        print ('robot.py -r <robot> -p <proc> -j <job>')
    for opt, arg in opts:
        if opt == '-h':
            print ('robot.py -r <robot> -p <proc> -j <job>')
        elif opt in ("-r", "--robot"):
            robot_no = arg
        elif opt in ("-p", "--proc"):
            proc_no = arg
        elif opt in ("-j", "--job"):
            job_no = arg
        elif opt in ("-i", "--input"):
            input_arg = arg
    pro = NewProject1(robot_no=robot_no,proc_no=proc_no,job_no=job_no,input_arg=input_arg)
    pro.Main()
