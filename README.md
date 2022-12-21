# download-canvas-files
Example using the Canvas API to download files, including directory structure and Canvas Modules.

* Clone this repo and install requirements.
* Identify a Canvas course from which you want to download files and make sure you have permissions.
* Create an API token through the settings menu for your user.
* Fill out `.env` variables (see below).
* Run `python downloader.py`

```
LOCAL_DIR = '~/Desktop/example_course/'
CANVAS_API_URL="https://institution.test.instructure.com/"
CANVAS_API_KEY="<you-api-key-retrieved-from-the-canvas-interface>"
CANVAS_EXAMPLE_COURSE_NUMBER=11111
```

### Running the downloader
Set your .env variables.

`python downloader.py`

The results will download all files found in the "files" section of a Canvas course to a specified local directory. If you have Google Drive installed on your local machine, files downloaded to a "watched" Google Drive folder will automatically sync those files to the cloud.

Note, this package also allows files to be downloaded by Module, but is currently turned off.

## Motivation
MIT OpenCourseWare freely publishes teaching materials to https://ocw.mit.edu. OCW has recently launched a new platform that streamlines publishing through a number of technology integrations, for example, utlizing Google Drive as the backend for content authors. OCW authors collect materials from faculty and instruction platforms across MIT and routinely need to share, collaborate, and modify materials before publishing to the web.

The Canvas LMS was introduced in 2020, and given Canvas has a robust set of APIs that allow programmatic access to teaching materials, it is worthwhile exploring how we can more easily transfer content from Canvas to OCW. Programmatically collecting teaching materials for OCW course authors would greatly reduce the overall time required to collect these materials, as well as, offer opportunities to programmatically explore materials before deciding to publish a course.

## API and CanvasAPI
Canvas has well established APIs for interacting with content and metadata. There are a number of third-party python packages supporting programmatic access to content and they are working on ways to make enhance access (e.g., GraphQL).

Canvas API docs: https://canvas.instructure.com/doc/api/

## What does this repo do?
The goal of this repo/script is to highlight how we can collect teaching materials from Canvas courses and sync them with the OCW publishing platform. This amounts to download files from a course and depositing them into a specific Google Drive folder.

Third-party python package used in this repo: https://canvasapi.readthedocs.io/en/stable/getting-started.html

### Assumptions
- You have access to a Canvas course and can [generate an API token](https://learninganalytics.ubc.ca/for-students/canvas-api/) from their settings menu.
- You have Google Drive installed locally on their machine, allowing for an automated sync to the Google Drive cloud.
  - One can also use this repo/script to simply download locally.
- You have python3 and can install requirements.

### Known Issues / Things to Work on
#### Downloading "files" and "files in their respective Modules"
All files are uploaded to the "files" section of a Canvas course. Files can also be linked to "Modules", which provides an easier to navigate experience for students. The API can provide file endpoints when parsing modules (i.e., linked pages, pdfs, etc within each module). Both the "files" section and the "Modules" representation can benefit an OCW author. 
- Issue: the current code duplicates files when downloading both the "files" and "module" representation. A possible solution would be to create symlinks in the module representation.
- Issue: the API currently cannot specify whether a module is "published" or "unpublished" (keep working with A. Roy).
- Issue: the current code orders Module folders (in the target location) by name, not the order in which they appear in Canvas. There is a field called "position" that provides the order of each module (e.g., position=2). One could incorporate a unique identifier [01], [02], [03] to order these modules for course authors.
