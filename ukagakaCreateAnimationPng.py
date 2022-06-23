import os
import glob
import cv2
import numpy as np

from configparser import ConfigParser

##default
CheckDirectory = "./AlphaIn"
OutputDirectory = "AlphaOut"
write_file = open('./surfaceXXXXX.txt', 'w' )
config_path = "./config.txt"


config = ConfigParser()
config.read( config_path )
core_section     = config[ 'core' ]

red     = int( core_section[ 'red' ] )
green   = int( core_section[ 'green' ] )
blue    = int( core_section[ 'blue' ] )



#surface番号の開始番号を指定する。
surface_start_num = int( core_section[ 'surface_start_num' ])
#surface element num
element_num = int( core_section[ 'element_num' ])
#アニメーションを表示時間を指定する。
animation_speed = int( core_section[ 'animation_speed' ])
#アニメーション番号を指定する。
animation_num = int( core_section[ 'animation_num' ])



if not os.path.exists( CheckDirectory ) :
    os.mkdir( CheckDirectory )
    sys.exit( "plz set picture : " + CheckDirectory )

if not os.path.exists( "./" + OutputDirectory ) :
    os.mkdir( "./" + OutputDirectory )

##animation
filelist = []
filelist.append("surface.append0 {" + '\n' )
filelist.append("\t" + str( animation_num ) + ".interval,sometimes" + '\n' )

##surfaceを定義
surfaceX = []
animation_count = 0


ReadDirectory = glob.glob( CheckDirectory + "/*.png" )
for file in ReadDirectory :
    file_name = os.path.basename( file )
    surfaceX.append( "surface" + str( surface_start_num ) + " {\n\telement" + str( element_num ) + ",overlay," + OutputDirectory + "/" + file_name + ",0,0\n}\n" )
    filelist.append("\tanimation" + str ( animation_num ) + ".pattern" + str( animation_count ) + ",overlay," + str( surface_start_num ) + "," + str( animation_speed ) + ",0,0" + '\n' )

    surface_start_num = surface_start_num +1
    animation_count = animation_count + 1

    img = cv2.imread( file , cv2.IMREAD_COLOR)
    ch_r, ch_g, ch_b = cv2.split(img[:,:,:3])
    #mask = np.zeros((img.shape[:3]), np.uint8)
    #mask = np.full( img.shape[:3] , 99 , np.uint8 )
    #指定色のマスクとして再構成する。
    #ch_r, ch_g, ch_b = cv2.split(mask[:,:,:3])
    #ch_r = np.full( ch_r.shape , color_R , np.uint8 )

    #( blue  , green , red )
    ch_a = cv2.inRange(img, ( blue , green , red) , ( blue , green , red ) )
    dst = cv2.merge((ch_r, ch_g, ch_b, cv2.bitwise_not(ch_a)))
    cv2.imwrite( "./" + OutputDirectory + "/" + file_name , dst )


filelist.append("}" + '\n' )
filelist.extend( surfaceX ) 
write_file.writelines( filelist  )

write_file.close()
#print( filelist )
print( "done" )


