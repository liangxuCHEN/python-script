 #-*- coding: utf-8 -*-
from qiniu import Auth, PersistentFop, build_op, op_save, urlsafe_base64_encode

#对已经上传到七牛的视频发起异步转码操作 
access_key = 'glxZuDgkuZ50X24oPkBP5vwO4DZ9Y2t9ujErMlqG'
secret_key = 'NcxhAi3WGmLYCEUIaPIsypk5zTgreM0bFi9WVsxY'
q = Auth(access_key, secret_key)

#要转码的文件所在的空间和文件名。
bucket = 'sfr-travel'
key = u'video/fighter2.avi'

#转码是使用的队列名称。
pipeline = 'travel-video'

#要进行转码的转码操作。
url = "http://7xoom6.com5.z0.glb.qiniucdn.com/logo-logo_piaoling.png"
url = urlsafe_base64_encode(url)
text = urlsafe_base64_encode("飘零旅游 www.ipiaoling.com")
font = urlsafe_base64_encode("微软雅黑")
color = urlsafe_base64_encode("#FFFFFF")
#fops = 'avthumb/mp4/s/640x360/vb/1.25m/wmImage/%s/wmGravity/%s' % (url, "Center")

fops = 'avthumb/mp4/s/640x360/vb/1.25m/wmText/%s/wmGravityText/%s/wmFontColor/%s/wmFontSize/15' % (
	text,
	"SouthWest",
	color
)
#可以对转码后的文件进行使用saveas参数自定义命名，当然也可以不指定文件会默认命名并保存在当前空间
saveas_key = urlsafe_base64_encode('sfr-travel:a_fighter_2')
fops = fops+'|saveas/'+saveas_key

pfop = PersistentFop(q, bucket, pipeline)
ops = []
ops.append(fops)
ret, info = pfop.execute(key, ops, 1)
print(info)
assert ret['persistentId'] is not None

