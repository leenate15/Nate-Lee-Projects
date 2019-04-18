# This script was written to perform a bulk copy and move of a given set of files to avoid performing the task manually.
import shutil

# I wrote down the numbers of all the pics in a text file and pasted them here -
# that's why I have to go through the conversion process
pic_nums = [3142,3143,3144,3156,3159,3163,3164,3169,3170,3178,3185,3193,\
		3195,3203,3206,3209,3212,3213,3214,3216,3217,3218,3225,3227,\
		3228,3234,3237,3238,3239,3240,3241,3243,3244,3245,3246,3248,\
		3249,3250,3251,3254,3266,3267,3277,3279,3280,3282,3283,3284,\
		3285,3289,3290,3291,3297,3298,3299,3306,3307,3309,3318,3320]

for num in pic_nums:
	pic_name = "DSC0" + str(num) + ".jpg" # Use the number to generate the file name
	shutil.copyfile("C:/Users/Nate/Desktop/Business/Guash/Photos/Fusion Jogger Night Shoot 1 - 04172019/"+pic_name,\
	"C:/Users/Nate/Desktop/Business/Guash/Photos/Fusion Jogger Night Shoot 1 - 04172019/Good Pics/"+pic_name)