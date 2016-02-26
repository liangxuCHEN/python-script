#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
import random
import time
import settings
import tool
from meminformation import meminfo

def init():
    dirver = webdriver.Firefox()
    return dirver

def login(dirver, name, password):
    dirver.get("https://mail.sina.com.cn/register/regmail.php")
    time.sleep(1)
    dirver.find_element_by_name('email').send_keys(name)
    dirver.find_element_by_name('psw').send_keys(password)

if __name__ == "__main__":
    logging = tool.log_init(model="a", file_name="sina_email")
    password = "qi0658214120"
    i = 5
    name_list = ["aaron","abbott","abel","abner","abraham","adair","adam","addison","adolph","adonis","adrian","ahern","alan","albert","aldrich","alexander","alfred","alger","algernon","allen","alston","alva","alvin","alvis","amos","andre","andrew","andy","angelo","augus","ansel","antony","antoine","antonio","archer","archibald","aries","arlen","armand","armstrong","arno","arnold","arthur","arvin","asa","ashbur","atwood","aubrey","august","augustine","avery","baird","baldwin","bancroft","bard","barlow","barnett","baron","barret","barry","bartholomew","bart","barton","bartley","basil","beacher","beau","beck","ben","benedict","benjamin","bennett","benson","berg","berger","bernard","bernie","bert","berton","bertram","bevis","bill","bing","bishop","blair","blake","blithe","bob","booth","borg","boris","bowen","boyce","boyd","bradley","brady","brandon","brian","broderick","brook","bruce","bruno","buck","burgess","burke","burnell","burton","byron","caesar","calvin","carey","carl","carr","carter","cash","cecil","cedric","chad","channing","chapman","charles","chasel","chester","christ","christian","christopher","clare","clarence","clark","claude","clement","cleveland","cliff","clifford","clyde","colbert","colby","colin","conrad","corey","cornelius","cornell","craig","curitis","cyril","dana","daniel","darcy","darnell","darren","dave","david","dean","dempsey","dennis","derrick","devin","dick","dominic","don","donahue","donald","douglas","drew","duke","duncan","dunn","dwight","dylan","earl","ed","eden","edgar","edmund","edison","edward","edwiin","egbert","eli","elijah","elliot","ellis","elmer","elroy","elton","elvis","emmanuel","enoch","eric","ernest","eugene","evan","everley","fabian","felix","ferdinand","fitch","fitzgerald","ford","francis","frank","franklin","frederic","gabriel","gale","gary","gavin","gene","geoffrey","geoff","george","gerald","gilbert","giles","glenn","goddard","godfery","gordon","greg","gregary","griffith","grover","gustave","guy","hale","haley","hamiltion","hardy","harlan","harley","harold","harriet","harry","harvey","hayden","heather","henry","herbert","herman","hilary","hiram","hobart","hogan","horace","howar","hubery","hugh","hugo","humphrey","hunter","hyman","ian","ingemar","ingram","ira","isaac","isidore","ivan","ives","jack","jacob","james","jared","jason","jay","jeff","jeffrey","jeremy","jerome","jerry","jesse","jim","jo","john","jonas","jonathan","joseph","joshua","joyce","julian","julius","justin","keith","kelly","ken","kennedy","kenneth","kent","kerr","kerwin","kevin","kim","king","kirk","kyle","lambert","lance","larry","lawrence","leif","len","lennon","leo","leonard","leopold","les","lester","levi","lewis","lionel","lou","louis","lucien","luther","lyle","lyndon","lynn","magee","malcolm","mandel","marcus","marico","mark","marlon","marsh","marshall","martin","marvin","matt","matthew","maurice","max","maximilian","maxwell","meredith","merle","merlin","michael","michell","mick","mike","miles","milo","monroe","montague","moore","morgan","mortimer","morton","moses","murphy","murray","myron","nat","nathan","nathaniel","neil","nelson","newman","nicholas","nick","nigel","noah","noel","norman","norton","ogden","oliver","omar","orville","osborn","oscar","osmond","oswald","otis","otto","owen","page","parker","paddy","patrick","paul","payne","perry","pete","peter","phil","philip","porter","prescott","primo","quentin","quennel","quincy","quinn","quintion","rachel","ralap","randolph","raymond","reg","regan","reginald","reuben","rex","richard","robert","robin","rock","rod","roderick","rodney","ron","ronald","rory","roy","rudolf","rupert","ryan","sam","sampson","samuel","sandy","saxon","scott","sean","sebastian","sid","sidney","silvester","simon","solomon","spencer","stan","stanford","stanley","steven","stev","steward","tab","taylor","ted","ternence","theobald","theodore","thomas","tiffany","tim","timothy","tobias","toby","todd","tom","tony","tracy","troy","truman","tyler","tyrone","ulysses","upton","uriah","valentine","valentine","verne","vic","victor","vincent","virgil","vito","vivian","wade","walker","walter","ward","warner","wayne","webb","webster","wendell","werner","wilbur","will","william","willie","winfred","winston","woodrow","wordsworth","wright","wythe","xavier","yale","yehudi","york","yves","zachary","zebulon","ziv"]
    max_num = len(name_list) - 1
    while i:
        dirver = init()
        time.sleep(2)
        name = name_list[random.randint(0, max_num)] + name_list[random.randint(0, max_num)] + str(time.time()).split(".")[0][-3:]
        if len(name) > 15 :
            name =  name[-14:]
        print name
        logging.info("name : " + name + "@sina.com ; password: " + password)
        login(dirver, name, password)
        i = i -1
