import requests


from datetime import datetime



date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


url = "http://192.168.1.64/ISAPI/System/time"

payload = "<?xml version: \"1.0\" encoding=\"UTF-8\"?><Time><timeMode>manual</timeMode><localTime>"+str(date)+"</localTime><timeZone>CST-4:00:00</timeZone></Time>"
headers = {
  'Content-Type': 'application/xml'
}

response = requests.request("PUT", url, headers=headers, data=payload,auth=requests.auth.HTTPDigestAuth("admin", "TEKTRON@123"))

print(response.text)

name = input('What is Name Of Camera\n') 



url = "http://192.168.1.64/ISAPI/System/Video/inputs/channels/1"

payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><VideoInputChannel xmlns=\"http://www.hikvision.com/ver20/XMLSchema\" version=\"2.0\"><id>1</id><inputPort>1</inputPort><name>"+str(name)+"</name><videoFormat>PAL</videoFormat></VideoInputChannel>"
headers = {
  'Content-Type': 'application/xml'
}

response = requests.request("PUT", url, headers=headers, data=payload,auth=requests.auth.HTTPDigestAuth("admin", "TEKTRON@123"))

print(response.text)

url = "http://192.168.1.64/ISAPI/System/Video/inputs/channels/1/overlays"

payload = "<?xml version: \"1.0\" encoding=\"utf-8\"?><VideoOverlay><normalizedScreenSize><normalizedScreenWidth>704</normalizedScreenWidth><normalizedScreenHeight>576</normalizedScreenHeight></normalizedScreenSize><attribute><transparent>false</transparent><flashing>false</flashing></attribute><fontSize>adaptive</fontSize><frontColorMode>auto</frontColorMode><alignment>customize</alignment><TextOverlayList><TextOverlay><id>1</id><enabled>false</enabled><alignment>0</alignment><positionX>0</positionX><positionY>576</positionY><displayText/></TextOverlay><TextOverlay><id>2</id><enabled>false</enabled><alignment>0</alignment><positionX>0</positionX><positionY>576</positionY><displayText/></TextOverlay><TextOverlay><id>3</id><enabled>false</enabled><alignment>0</alignment><positionX>0</positionX><positionY>576</positionY><displayText/></TextOverlay><TextOverlay><id>4</id><enabled>false</enabled><alignment>0</alignment><positionX>0</positionX><positionY>576</positionY><displayText/></TextOverlay></TextOverlayList><DateTimeOverlay><enabled>true</enabled><positionY>545</positionY><positionX>0</positionX><dateStyle>CHR-DD/MM/YYYY</dateStyle><timeStyle>24hour</timeStyle><displayWeek>true</displayWeek></DateTimeOverlay><channelNameOverlay><enabled>true</enabled><positionY>65</positionY><positionX>512</positionX></channelNameOverlay></VideoOverlay>"
headers = {
  'Content-Type': 'application/xml'
}

response = requests.request("PUT", url, headers=headers, data=payload,auth=requests.auth.HTTPDigestAuth("admin", "TEKTRON@123"))

print(response.text)


url = "http://192.168.1.64/ISAPI/ContentMgmt/record/tracks"

payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><TrackList xmlns=\"http://www.hikvision.com/ver20/XMLSchema\" version=\"2.0\">\r\n<Track xmlns=\"http://www.hikvision.com/ver20/XMLSchema\" version=\"2.0\">\r\n<id>101</id>\r\n<Channel>101</Channel>\r\n<Enable>true</Enable>\r\n<Description>trackType=standard,trackType=video,codecType=H.264-BP,resolution=1920x1080,framerate=1.960000 fps,bitrate=4096 kbps</Description>\r\n<TrackGUID>e32e6863-ea5e-4ee4-997e-bc5e337b47e3</TrackGUID>\r\n<DefaultRecordingMode>CMR</DefaultRecordingMode>\r\n<LoopEnable>true</LoopEnable>\r\n<SrcDescriptor>\r\n<SrcGUID>e32e6863-ea5e-4ee4-997e-bc5e337b47e3</SrcGUID>\r\n<SrcChannel>1</SrcChannel>\r\n<StreamHint>trackType=standard,trackType=video,codecType=H.264-BP,resolution=1920x1080,framerate=1.960000 fps,bitrate=4096 kbps</StreamHint>\r\n<SrcDriver>RTSP</SrcDriver>\r\n<SrcType>H.264-BP</SrcType>\r\n<SrcUrl>rtsp://localhost/PSIA/Streaming/channels/101</SrcUrl>\r\n<SrcType>DESCRIBE, SETUP, PLAY, TEARDOWN</SrcType>\r\n<SrcLogin>0b2e400fed3a02ecc7f9c2b8d36079ce</SrcLogin>\r\n</SrcDescriptor><TrackSchedule xmlns=\"\"><ScheduleBlockList><ScheduleBlock><ScheduleBlockGUID>{00000000-0000-0000-0000-000000000000}</ScheduleBlockGUID><ScheduleBlockType>www.std-cgi.com/racm/schedule/ver10</ScheduleBlockType><ScheduleAction><id>1</id><ScheduleActionStartTime><DayOfWeek>Monday</DayOfWeek><TimeOfDay>00:00:00</TimeOfDay></ScheduleActionStartTime><ScheduleActionEndTime><DayOfWeek>Monday</DayOfWeek><TimeOfDay>24:00:00</TimeOfDay></ScheduleActionEndTime><ScheduleDSTEnable>false</ScheduleDSTEnable><Description>nothing</Description><Actions><Record>true</Record><Log>false</Log><SaveImg>false</SaveImg><ActionRecordingMode>CMR</ActionRecordingMode></Actions></ScheduleAction><ScheduleAction><id>2</id><ScheduleActionStartTime><DayOfWeek>Tuesday</DayOfWeek><TimeOfDay>00:00:00</TimeOfDay></ScheduleActionStartTime><ScheduleActionEndTime><DayOfWeek>Tuesday</DayOfWeek><TimeOfDay>24:00:00</TimeOfDay></ScheduleActionEndTime><ScheduleDSTEnable>false</ScheduleDSTEnable><Description>nothing</Description><Actions><Record>true</Record><Log>false</Log><SaveImg>false</SaveImg><ActionRecordingMode>CMR</ActionRecordingMode></Actions></ScheduleAction><ScheduleAction><id>3</id><ScheduleActionStartTime><DayOfWeek>Wednesday</DayOfWeek><TimeOfDay>00:00:00</TimeOfDay></ScheduleActionStartTime><ScheduleActionEndTime><DayOfWeek>Wednesday</DayOfWeek><TimeOfDay>24:00:00</TimeOfDay></ScheduleActionEndTime><ScheduleDSTEnable>false</ScheduleDSTEnable><Description>nothing</Description><Actions><Record>true</Record><Log>false</Log><SaveImg>false</SaveImg><ActionRecordingMode>CMR</ActionRecordingMode></Actions></ScheduleAction><ScheduleAction><id>4</id><ScheduleActionStartTime><DayOfWeek>Thursday</DayOfWeek><TimeOfDay>00:00:00</TimeOfDay></ScheduleActionStartTime><ScheduleActionEndTime><DayOfWeek>Thursday</DayOfWeek><TimeOfDay>24:00:00</TimeOfDay></ScheduleActionEndTime><ScheduleDSTEnable>false</ScheduleDSTEnable><Description>nothing</Description><Actions><Record>true</Record><Log>false</Log><SaveImg>false</SaveImg><ActionRecordingMode>CMR</ActionRecordingMode></Actions></ScheduleAction><ScheduleAction><id>5</id><ScheduleActionStartTime><DayOfWeek>Friday</DayOfWeek><TimeOfDay>00:00:00</TimeOfDay></ScheduleActionStartTime><ScheduleActionEndTime><DayOfWeek>Friday</DayOfWeek><TimeOfDay>24:00:00</TimeOfDay></ScheduleActionEndTime><ScheduleDSTEnable>false</ScheduleDSTEnable><Description>nothing</Description><Actions><Record>true</Record><Log>false</Log><SaveImg>false</SaveImg><ActionRecordingMode>CMR</ActionRecordingMode></Actions></ScheduleAction><ScheduleAction><id>6</id><ScheduleActionStartTime><DayOfWeek>Saturday</DayOfWeek><TimeOfDay>00:00:00</TimeOfDay></ScheduleActionStartTime><ScheduleActionEndTime><DayOfWeek>Saturday</DayOfWeek><TimeOfDay>24:00:00</TimeOfDay></ScheduleActionEndTime><ScheduleDSTEnable>false</ScheduleDSTEnable><Description>nothing</Description><Actions><Record>true</Record><Log>false</Log><SaveImg>false</SaveImg><ActionRecordingMode>CMR</ActionRecordingMode></Actions></ScheduleAction><ScheduleAction><id>7</id><ScheduleActionStartTime><DayOfWeek>Sunday</DayOfWeek><TimeOfDay>00:00:00</TimeOfDay></ScheduleActionStartTime><ScheduleActionEndTime><DayOfWeek>Sunday</DayOfWeek><TimeOfDay>24:00:00</TimeOfDay></ScheduleActionEndTime><ScheduleDSTEnable>false</ScheduleDSTEnable><Description>nothing</Description><Actions><Record>true</Record><Log>false</Log><SaveImg>false</SaveImg><ActionRecordingMode>CMR</ActionRecordingMode></Actions></ScheduleAction></ScheduleBlock></ScheduleBlockList></TrackSchedule>\r\n\r\n<CustomExtensionList>\r\n<CustomExtension>\r\n<CustomExtensionName>www.hikvision.com/RaCM/trackExt/ver10</CustomExtensionName>\r\n<enableSchedule>true</enableSchedule>\r\n<PreRecordTimeSeconds>5</PreRecordTimeSeconds>\r\n<PostRecordTimeSeconds>5</PostRecordTimeSeconds>\r\n</CustomExtension>\r\n</CustomExtensionList>\r\n<Duration>P7DT0H</Duration>\r\n<durationEnabled>false</durationEnabled>\r\n</Track>\r\n\r\n</TrackList>"
headers = {
  'Content-Type': 'application/xml'
}

response = requests.request("PUT", url, headers=headers, data=payload,auth=requests.auth.HTTPDigestAuth("admin", "TEKTRON@123"))

print(response.text)



url = "http://192.168.1.64/ISAPI/ContentMgmt/Storage/quota/1"

payload = "<?xml version: \"1.0\" encoding=\"UTF-8\"?><diskQuota xmlns=\"http://www.hikvision.com/ver20/XMLSchema\" version=\"2.0\">\r\n<id>1</id>\r\n<type>ratio</type>\r\n<videoQuotaRatio>95</videoQuotaRatio>\r\n<totalVideoVolume>0</totalVideoVolume>\r\n<freeVideoQuota>0</freeVideoQuota>\r\n<pictureQuotaRatio>5</pictureQuotaRatio>\r\n<totalPictureVolume>0</totalPictureVolume>\r\n<freePictureQuota>0</freePictureQuota>\r\n</diskQuota>"
headers = {
  'Content-Type': 'application/xml'
}

response = requests.request("PUT", url, headers=headers, data=payload,auth=requests.auth.HTTPDigestAuth("admin", "TEKTRON@123"))

print(response.text)


print("Wait While Formatting to be finish it will take 2-3 Mins")
url = "http://192.168.1.64/ISAPI/ContentMgmt/Storage/hdd/1/format/?formatType=EXT4"

payload = {}
headers = {}

response = requests.request("PUT", url, headers=headers, data=payload,auth=requests.auth.HTTPDigestAuth("admin", "TEKTRON@123"))


print(response.text)



url = "http://192.168.1.64/ISAPI/ContentMgmt/Storage"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload,auth=requests.auth.HTTPDigestAuth("admin", "TEKTRON@123"))

print(response.text)
