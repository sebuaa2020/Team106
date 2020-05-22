class navigation:
    #https://baijiahao.baidu.com/s?id=1666716958851993517&wfr=spider&for=pc
    def set_cur_pos(self):
        return
        x=0
        y=0
        send_simple_goal(x,y)#有一个cpp版的
    def set_tar_pos(self):
        pass
    def navigate(self):
        return 
        os.system("gnome-terminal -e 'bash -c \"rosrun wpr_simulation wpb_navigation; exec bash\"'")
