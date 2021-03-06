from django.shortcuts import render

<<<<<<< HEAD
album_sizes={"architecture":25,"landscapes":18,"wildlife":24,"nature":24,"toronto":29,"montreal":80,"madagascar":140,"vosges":14,"london":76,"seattle":30}
=======
album_sizes={"architecture":16,"landscapes":18,"wildlife":24,"nature":24,"toronto":34,"montreal":80,"madagascar":140,"vosges":14,"london":76,"seattle":30,'amsterdam':56}
>>>>>>> fa53654a1fd01a834c5120502e01bb7bd5cc9111
#album_titles={"toronto":"Toronto","montreal":"Montreal"}
album_names=["architecture","landscapes","wildlife","nature","toronto","montreal","madagascar", "vosges","london",'amsterdam',"seattle"] #album_sizes.keys() returns keys sorted alphabetically
picture_paths= []

def home(request):
    context = {}
    return render(request,'photos/home.html',context)

def aboutme(request):
    context = {}
    return render(request,'photos/aboutme.html',context)

def gallery(request,album_name):
    context = {'album_name':album_name}
    if (album_names.count(album_name) == 0):
        return render(request,'photos/error404.html',context)
    else:
        generatePicturePaths(album_name)
        prevNext = getPreviousAndNext(album_name)
        context['pictures']=picture_paths
        context['previous']=prevNext[0]
        context['next']=prevNext[1]
        return render(request,'photos/gallery.html',context)

def pageNotFound(request,album_name):
    context = {'album_name':album_name}
    return render(request,'photos/error404.html',context)


#######################################################################################
####                    Helper functions
#######################################################################################


#######################################################################################
####    generatePicturePath: updates array picture_paths with the appropriate
####                         picture folder and name.
#######################################################################################
def generatePicturePaths(name):
    del picture_paths[0:len(picture_paths)] 
    for x in range(1,album_sizes[name]+1):
        large =  'photos/media/'+name+'/large/'+name+'-'+str(x)+'.jpg'
<<<<<<< HEAD
        small =  'photos/media/'+name+'/small/'+name+'-'+str(x)+'.jpg'
        picture_paths.append((large,small))
=======
        thumb =  'photos/media/'+name+'/small/'+name+'-'+str(x)+'.jpg'
        picture_paths.append((large,thumb))
>>>>>>> fa53654a1fd01a834c5120502e01bb7bd5cc9111

#######################################################################################


#######################################################################################
####    getPreviousAndNext: returns a tuple with the names of the albums preceding and
####                        following the current album (with wraparound), and aready
####                        formatted with first letter uppercases
#######################################################################################
def getPreviousAndNext(name):
    i = album_names.index(name)
    
    if i+1<len(album_names):
        next_album = album_names[i+1]
    else:
        next_album=album_names[0] #wwaparound

    if i>0:
        prev_album = album_names[i-1]
    else:
        prev_album = album_names[len(album_names)-1] #wraparound
   
    #prev_album = album_titles[prev_album]
    #next_album = album_titles[next_album]

    return (prev_album,next_album)
#######################################################################################
