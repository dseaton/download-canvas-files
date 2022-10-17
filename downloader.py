from pathlib import Path


class Downloader(object):
    def __init__(self, course, local_download_dir):
        local_download_dir = local_download_dir
        self.base_files_path = local_download_dir
        # self.module_lookup = self.create_module_folders()
        self.folder_lookup = self.create_file_folders()
        print(course.id, local_download_dir)
        self.get_files()       
    
    def create_file_folders(self):
        folder_lookup = dict()
        for f in course.get_folders():
            folder_name = f.full_name.lstrip('course ')
            Path(self.base_files_path + folder_name).mkdir(parents=True, exist_ok=True) 
            folder_lookup[f.id] = folder_name
        
        return folder_lookup
            
    def get_files(self):
        files = [f for f in course.get_files()]
        for f in files:
            loc = self.base_files_path + self.folder_lookup[f.folder_id] + '/' + f.display_name
            print(loc)
            request.urlretrieve(f.url, filename=loc)
            
    def create_module_folders(self):
        module_lookup = dict()
        for m in course.get_modules():
            module_name = m.name
            Path(self.base_files_path + module_name).mkdir(parents=True, exist_ok=True) 
            
            for i in m.get_module_items():
                if i.type == 'File':
                    f = course.get_file(i.content_id)
                    loc = self.base_files_path + module_name + '/' + str(i.position) + '_' + f.display_name
                    request.urlretrieve(f.url, filename=loc)
                elif i.type == 'Page':
                    p = course.get_page(i.page_url)
                    loc = self.base_files_path + module_name + '/' + str(i.position) + '_' + p.title
                    request.urlretrieve(p.html_url, filename=loc)
                else:
                    print(i.type, i.title)
            
            module_lookup[m.id] = module_name
        
        return module_lookup


if __name__ == "__main__":
    '''
    Examples of downloading files/content from a Canvas course.
    .env variables are set to:
      - LOCAL_DOWNLOAD_DIR: Download files to a local directory. I have a local Google Drive folder (which syncs automatically).
      - CANVAS_API_URL: URL where we will "get" content.
      - CANVAS_API_KEY: API key generated through the Canvas settings interface.
      - CANVAS_EXAMPLE_COURSE_NUMBER: the course number found in a Canvas URL (e.g., https://canvas.instructure.com/courses/2066466).
    '''
    import os
    from dotenv import load_dotenv
    import urllib.request as request
    from canvasapi import Canvas

    load_dotenv()
    canvas = Canvas(os.getenv('CANVAS_API_URL'), os.getenv('CANVAS_API_KEY'))
    course = canvas.get_course(os.getenv('CANVAS_EXAMPLE_COURSE_NUMBER'))
    Downloader(course, os.getenv('LOCAL_DOWNLOAD_DIR'))
