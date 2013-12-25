IMGCreator
==========

Python app used to generate the html for use with a photo gallery (like highslide) with user determined src &amp; href 

I threw this together today for at the request of someone who uses highslide for a community website. He was annoyed that highslide did not allow subfolders when using their software to generate the html code for the images and didn't want to have to go through and change hundreds of href's and src's every time he needed to add more photos. This app has the user enter the local path that contains the photos to upload (the browse button can be used for this) and a manual entry of the destination path. So if you want to upload your photos to a subfolder of an Images folder, you would enter Images/FooBar as the destination path. 

Hitting submit will create a yourcode.txt in the same dir as the app. This is specific right now to highslide, and the entire photo gallery div is ready to be copied and pasted onto the html page.

Note: This is specific to a thumbnail gallery, so if you are putting your photos in Images/Test, put the originals in a subfolder called "Large" and the thumbnails in a subfolder called "Small" within Test. Don't specify these in the app, it automatically places Large and Small in the proper href &amp; src.
