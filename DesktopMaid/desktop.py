import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

folder_to_track = '/Users/Babi/Desktop'
folder_destination = '/Users/Babi/Desktop/Babi'

extensions_folders = {
#No name
    'noname' : "/Users/Babi/Desktop/Babi/Other/Uncategorized",
#Audio
    '.aif' : "/Users/Babi/Desktop/Babi/Media/Audio",
    '.cda' : "/Users/Babi/Desktop/Babi/Media/Audio",
    '.mid' : "/Users/Babi/Desktop/Babi/Media/Audio",
    '.midi' : "/Users/Babi/Desktop/Babi/Media/Audio",
    '.mp3' : "/Users/Babi/Desktop/Babi/Media/Audio",
    '.mpa' : "/Users/Babi/Desktop/Babi/Media/Audio",
    '.ogg' : "/Users/Babi/Desktop/Babi/Media/Audio",
    '.wav' : "/Users/Babi/Desktop/Babi/Media/Audio",
    '.wma' : "/Users/Babi/Desktop/Babi/Media/Audio",
    '.wpl' : "/Users/Babi/Desktop/Babi/Media/Audio",
    '.m3u' : "/Users/Babi/Desktop/Babi/Media/Audio",
#Text
    '.txt' : "/Users/Babi/Desktop/Babi/Text/TextFiles",
    '.doc' : "/Users/Babi/Desktop/Babi/Text/Microsoft/Word",
    '.docx' : "/Users/Babi/Desktop/Babi/Text/Microsoft/Word",
    '.odt ' : "/Users/Babi/Desktop/Babi/Text/TextFiles",
    '.pdf': "/Users/Babi/Desktop/Babi/Text/PDF",
    '.rtf': "/Users/Babi/Desktop/Babi/Text/TextFiles",
    '.tex': "/Users/Babi/Desktop/Babi/Text/TextFiles",
    '.wks ': "/Users/Babi/Desktop/Babi/Text/TextFiles",
    '.wps': "/Users/Babi/Desktop/Babi/Text/TextFiles",
    '.wpd': "/Users/Babi/Desktop/Babi/Text/TextFiles",
#Video
    '.3g2': "/Users/Babi/Desktop/Babi/Media/Video",
    '.3gp': "/Users/Babi/Desktop/Babi/Media/Video",
    '.avi': "/Users/Babi/Desktop/Babi/Media/Video",
    '.flv': "/Users/Babi/Desktop/Babi/Media/Video",
    '.h264': "/Users/Babi/Desktop/Babi/Media/Video",
    '.m4v': "/Users/Babi/Desktop/Babi/Media/Video",
    '.mkv': "/Users/Babi/Desktop/Babi/Media/Video",
    '.mov': "/Users/Babi/Desktop/Babi/Media/Video",
    '.mp4': "/Users/Babi/Desktop/Babi/Media/Video",
    '.mpg': "/Users/Babi/Desktop/Babi/Media/Video",
    '.mpeg': "/Users/Babi/Desktop/Babi/Media/Video",
    '.rm': "/Users/Babi/Desktop/Babi/Media/Video",
    '.swf': "/Users/Babi/Desktop/Babi/Media/Video",
    '.vob': "/Users/Babi/Desktop/Babi/Media/Video",
    '.wmv': "/Users/Babi/Desktop/Babi/Media/Video",
#Images
    '.ai': "/Users/Babi/Desktop/Babi/Media/Images",
    '.bmp': "/Users/Babi/Desktop/Babi/Media/Images",
    '.gif': "/Users/Babi/Desktop/Babi/Media/Images",
    '.ico': "/Users/Babi/Desktop/Babi/Media/Images",
    '.jpg': "/Users/Babi/Desktop/Babi/Media/Images",
    '.jpeg': "/Users/Babi/Desktop/Babi/Media/Images",
    '.png': "/Users/Babi/Desktop/Babi/Media/Images",
    '.ps': "/Users/Babi/Desktop/Babi/Media/Images",
    '.psd': "/Users/Babi/Desktop/Babi/Media/Images",
    '.svg': "/Users/Babi/Desktop/Babi/Media/Images",
    '.tif': "/Users/Babi/Desktop/Babi/Media/Images",
    '.tiff': "/Users/Babi/Desktop/Babi/Media/Images",
    '.CR2': "/Users/Babi/Desktop/Babi/Media/Images",
#Internet
    '.asp': "/Users/Babi/Desktop/Babi/Other/Internet",
    '.aspx': "/Users/Babi/Desktop/Babi/Other/Internet",
    '.cer': "/Users/Babi/Desktop/Babi/Other/Internet",
    '.cfm': "/Users/Babi/Desktop/Babi/Other/Internet",
    '.cgi': "/Users/Babi/Desktop/Babi/Other/Internet",
    '.pl': "/Users/Babi/Desktop/Babi/Other/Internet",
    '.css': "/Users/Babi/Desktop/Babi/Other/Internet",
    '.htm': "/Users/Babi/Desktop/Babi/Other/Internet",
    '.js': "/Users/Babi/Desktop/Babi/Other/Internet",
    '.jsp': "/Users/Babi/Desktop/Babi/Other/Internet",
    '.part': "/Users/Babi/Desktop/Babi/Other/Internet",
    '.php': "/Users/Babi/Desktop/Babi/Other/Internet",
    '.rss': "/Users/Babi/Desktop/Babi/Other/Internet",
    '.xhtml': "/Users/Babi/Desktop/Babi/Other/Internet",
#Compressed
    '.7z': "/Users/Babi/Desktop/Babi/Other/Compressed",
    '.arj': "/Users/Babi/Desktop/Babi/Other/Compressed",
    '.deb': "/Users/Babi/Desktop/Babi/Other/Compressed",
    '.pkg': "/Users/Babi/Desktop/Babi/Other/Compressed",
    '.rar': "/Users/Babi/Desktop/Babi/Other/Compressed",
    '.rpm': "/Users/Babi/Desktop/Babi/Other/Compressed",
    '.tar.gz': "/Users/Babi/Desktop/Babi/Other/Compressed",
    '.z': "/Users/Babi/Desktop/Babi/Other/Compressed",
    '.zip': "/Users/Babi/Desktop/Babi/Other/Compressed",
#Disc
    '.bin': "/Users/Babi/Desktop/Babi/Other/Disc",
    '.dmg': "/Users/Babi/Desktop/Babi/Other/Disc",
    '.iso': "/Users/Babi/Desktop/Babi/Other/Disc",
    '.toast': "/Users/Babi/Desktop/Babi/Other/Disc",
    '.vcd': "/Users/Babi/Desktop/Babi/Other/Disc",
#Data
    '.csv': "/Users/Babi/Desktop/Babi/Programming/Database",
    '.dat': "/Users/Babi/Desktop/Babi/Programming/Database",
    '.db': "/Users/Babi/Desktop/Babi/Programming/Database",
    '.dbf': "/Users/Babi/Desktop/Babi/Programming/Database",
    '.log': "/Users/Babi/Desktop/Babi/Programming/Database",
    '.mdb': "/Users/Babi/Desktop/Babi/Programming/Database",
    '.sav': "/Users/Babi/Desktop/Babi/Programming/Database",
    '.sql': "/Users/Babi/Desktop/Babi/Programming/Database",
    '.tar': "/Users/Babi/Desktop/Babi/Programming/Database",
    '.xml': "/Users/Babi/Desktop/Babi/Programming/Database",
    '.json': "/Users/Babi/Desktop/Babi/Programming/Database",
#Executables
    '.apk': "/Users/Babi/Desktop/Babi/Other/Executables",
    '.bat': "/Users/Babi/Desktop/Babi/Other/Executables",
    '.com': "/Users/Babi/Desktop/Babi/Other/Executables",
    '.exe': "/Users/Babi/Desktop/Babi/Other/Executables",
    '.gadget': "/Users/Babi/Desktop/Babi/Other/Executables",
    '.jar': "/Users/Babi/Desktop/Babi/Other/Executables",
    '.wsf': "/Users/Babi/Desktop/Babi/Other/Executables",
#Fonts
    '.fnt': "/Users/Babi/Desktop/Babi/Other/Fonts",
    '.fon': "/Users/Babi/Desktop/Babi/Other/Fonts",
    '.otf': "/Users/Babi/Desktop/Babi/Other/Fonts",
    '.ttf': "/Users/Babi/Desktop/Babi/Other/Fonts",
#Presentations
    '.key': "/Users/Babi/Desktop/Babi/Text/Presentations",
    '.odp': "/Users/Babi/Desktop/Babi/Text/Presentations",
    '.pps': "/Users/Babi/Desktop/Babi/Text/Presentations",
    '.ppt': "/Users/Babi/Desktop/Babi/Text/Presentations",
    '.pptx': "/Users/Babi/Desktop/Babi/Text/Presentations",
#Programming
    '.c': "/Users/Babi/Desktop/Babi/Programming/C&C++",
    '.class': "/Users/Babi/Desktop/Babi/Programming/Java",
    '.dart': "/Users/Babi/Desktop/Babi/Programming/Dart",
    '.py': "/Users/Babi/Desktop/Babi/Programming/Python",
    '.sh': "/Users/Babi/Desktop/Babi/Programming/Shell",
    '.swift': "/Users/Babi/Desktop/Babi/Programming/Swift",
    '.html': "/Users/Babi/Desktop/Babi/Programming/C&C++",
    '.h': "/Users/Babi/Desktop/Babi/Programming/C&C++",
#Spreadsheets
    '.ods' : "/Users/Babi/Desktop/Babi/Text/Microsoft/Excel",
    '.xlr' : "/Users/Babi/Desktop/Babi/Text/Microsoft/Excel",
    '.xls' : "/Users/Babi/Desktop/Babi/Text/Microsoft/Excel",
    '.xlsx' : "/Users/Babi/Desktop/Babi/Text/Microsoft/Excel",
#System
    '.bak' : "/Users/Babi/Desktop/Babi/Text/Other/System",
    '.cab' : "/Users/Babi/Desktop/Babi/Text/Other/System",
    '.cfg' : "/Users/Babi/Desktop/Babi/Text/Other/System",
    '.cpl' : "/Users/Babi/Desktop/Babi/Text/Other/System",
    '.cur' : "/Users/Babi/Desktop/Babi/Text/Other/System",
    '.dll' : "/Users/Babi/Desktop/Babi/Text/Other/System",
    '.dmp' : "/Users/Babi/Desktop/Babi/Text/Other/System",
    '.drv' : "/Users/Babi/Desktop/Babi/Text/Other/System",
    '.icns' : "/Users/Babi/Desktop/Babi/Text/Other/System",
    '.ico' : "/Users/Babi/Desktop/Babi/Text/Other/System",
    '.ini' : "/Users/Babi/Desktop/Babi/Text/Other/System",
    '.lnk' : "/Users/Babi/Desktop/Babi/Text/Other/System",
    '.msi' : "/Users/Babi/Desktop/Babi/Text/Other/System",
    '.sys' : "/Users/Babi/Desktop/Babi/Text/Other/System",
    '.tmp' : "/Users/Babi/Desktop/Babi/Text/Other/System",
}


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            iter = 1
            if filename != 'Babi':
                new_name = filename
                extension = 'noname'
                try:
                    extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                    path = extensions_folders[extension]
                except Exception:
                    extension = 'noname'

                time_now = datetime.now()
                year = time_now.strftime("%Y")
                month = time_now.strftime("%m")

                folder_dest_path = extensions_folders[extension]

                year_exists = False
                month_exists = False
                for folder_name in os.listdir(extensions_folders[extension]):
                    if folder_name == year:
                        folder_dest_path = extensions_folders[extension] + "/" + year
                        year_exists = True
                        for folder_month in os.listdir(folder_dest_path):
                            if month == folder_month:
                                folder_dest_path = extensions_folders[extension] + "/" + year + "/" + month
                                month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_dest_path = extensions_folders[extension] + "/" + year + "/"
                    if not month_exists:
                        os.mkdir(folder_dest_path + "/" + month)
                        folder_dest_path = folder_dest_path + "/" + month

                    file_exists = os.path.isfile(folder_dest_path + "/" + new_name)
                    while file_exists:
                        iter += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(iter) + os.path.splitext(
                            folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_dest_path + "/" + new_name)
                    source = folder_to_track + "/" + new_name
                    os.rename(source, new_name)


event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
