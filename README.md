# Copy Xbox Gamepass Games on Windows Pc
The main problem with gamepass games is the protected .exe files, if we could copy them this guide wouldn't exist, i tried finding anything online about this but i couldn't, so i made this guide.
this guide is a stupid workaround, we simply download the .exe and copy the rest of the files.

## Requirements
This will depend on the game you want to copy, to know for sure we need to look for the download times of the exes in perspective to the first file downloaded,
go to where the game is downloaded, you will find the following structure:

![Screenshot 2023-04-08 221309](https://user-images.githubusercontent.com/88838071/230740958-ba382d6e-9fd9-4408-a149-73f400054fed.png)

Look at the date of the .xsp file this is the start of download date.

The file without an extension is the end of download date.

All game files are in Content folder, look for the main executable(.exe) inside and look at the date.

![Screenshot 2023-04-08 221840 copy](https://user-images.githubusercontent.com/88838071/230741124-f2823530-e8de-4863-8fb7-4cd71692aa5f.png)

By comparing the dates we should know when is the .exe downloaded, then follow the corresponding guide:


## If .exe is downloaded in the start

The easiest one, simply start downloading on the other pc until the .exe is downloaded (make sure it's completele downloaded as the file is created before it's fully downloaded).

Pasue the download and copy all the other files you already downloaded.

Note that if some files refuse to be copied it's most likely the download is not paused.

Resume the download and the game should be downloaded.

if download fails at 100%, this normal just resume once more, if it still fails go to the root folder of the current drive you will find a folder called WpSystem, rename it to WpSystem.old (there is save date inside return them after download is complete).

## If .exe is not downloaded at start

If the game is already downloaded it's too late, this needs to be done before it's downloaded.

both devices need to have the same exact location download location.

The progress of the download is stored in the .xvi file, we will use the backup script to make a copy of this file every 2 minutes.

if the .exe is downloaded at an earlier time, we will also need the .xvi file from when the game is fully installed, back it up after the download is done.

![Screenshot 2023-04-08 221309](https://user-images.githubusercontent.com/88838071/230741880-8d41a4b8-cdda-49f6-9884-7ae69f5c815f.png)

[Download and run the python script](https://github.com/MoazSalem/Timed_Backup/releases/download/v1.0/backup.exe)

![Screenshot 2023-04-08 223737](https://user-images.githubusercontent.com/88838071/230741631-b7fb9c41-c912-4a29-9efd-a356b4060137.png)

Start downloading the game, in the script gui press browse and select the .xvi file, then press start this will backup the file every 2 minutes in a folder named backup besides the script.

After the game is fully downloaded stop the script, find the .exe file and look at the date(time of download assume it's 6:20pm).

Go back the script, open backup folder you will find folders named with the time of the backup, open the closest number to the download time of the .exe, For 6:20pm the folder will be named  18-20 (could be before it 6:19pm so it will be named 18-19), inside the folder is the file we need.

We will use this file to change the download progress in the other pc to right before the .exe is downloaded.

Now Moving to the other device.

Copy the game to the other pc (needs to be the same exact location).

Replace the .xvi file with the backed up one (before the .exe is downloaded).

Open xbox app and start downloading the game in the same location (note that it can some times halucinante if the game is on the external hdd so remove the hdd first).

It will see the game and start download from right before the .exe is downloaded

If it was near the end then we are done, resume download and let it finish.

Else pause the download, replace the .xvi file from the completely downloaded game to skip to the end of the download.

And we are done, resume download and it should be finished.

Note that if some files refuse to be copied it's most likely the download is not paused.

If the game is not working recopy all files again.

if download fails at 100%, this normal just resume once more, if it still fails go to the root folder of the current drive you will find a folder called WpSystem, rename it to WpSystem.old (there is save date inside return them after download is complete).
