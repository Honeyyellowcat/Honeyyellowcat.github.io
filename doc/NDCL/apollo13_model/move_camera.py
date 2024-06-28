import bpy
import os
import csv
import mathutils
import math

output_dir = 'C:\\Users\\trail\\Documents\\School\\NDCL\\camera_move_output'
input_file = 'C:\\Users\\trail\\Documents\\School\\NDCL\\Positions.csv'

def convert_to_gif():
    os.system("ffmpeg -f image2 -i " + output_dir + "\\render%d.png video.avi")
    os.system("ffmpeg -i video.avi -pix_fmt rgb8 " + output_dir + "\\out.gif")

def camera_step():
    global step
    global steps
    global point
    global pos_data
    
    global start_point
    global end_point
    global start_rot
    global end_rot
    
    global image_num
    
    # Set camera rotation
    scene.camera.rotation_quaternion = start_rot.slerp(end_rot, float(step)/steps)

    # Set camera translation
    scene.camera.location.x = start_point.x + ((end_point.x - start_point.x) * (float(step)/steps))
    scene.camera.location.y = start_point.y + ((end_point.y - start_point.y) * (float(step)/steps))
    scene.camera.location.z = start_point.z + ((end_point.z - start_point.z) * (float(step)/steps))
    
    output_file_pattern_string='render%d.png'
    
    bpy.context.scene.render.filepath = os.path.join(output_dir, output_file_pattern_string % (image_num))
    bpy.ops.render.render(write_still=True)
    
    step = step + 1
    image_num = image_num + 1
    
    if step == steps and point < len(pos_data)-2:# end of this segment, not the second to last point in the list
        step = 0
        point = point + 1
        # set start and end to the current and next
        bpy.data.objects['Start Point'].location = mathutils.Vector((pos_data[point][0], pos_data[point][1], pos_data[point][2]))
        bpy.data.objects['End Point'].location = mathutils.Vector((pos_data[point+1][0], pos_data[point+1][1], pos_data[point+1][2]))
        start_quat = mathutils.Euler((math.radians(pos_data[point][3]), math.radians(pos_data[point][4]), math.radians(pos_data[point][5])), 'XYZ').to_quaternion()
        end_quat = mathutils.Euler((math.radians(pos_data[point+1][3]), math.radians(pos_data[point+1][4]), math.radians(pos_data[point+1][5])), 'XYZ').to_quaternion()
        bpy.data.objects['Start Point'].rotation_quaternion = start_quat
        bpy.data.objects['End Point'].rotation_quaternion = end_quat
        
        # get start and end pos and rot from start and end objects
        start_point = bpy.data.objects['Start Point'].location
        end_point = bpy.data.objects['End Point'].location
        start_rot = bpy.data.objects['Start Point'].rotation_quaternion
        end_rot = bpy.data.objects['End Point'].rotation_quaternion
    
    if step == steps and point == len(pos_data)-2:# end of this segment and second to last point in the list
        convert_to_gif()
        return None
    else:
        return 0.00

pos_data = []

with open(input_file, newline='', encoding='utf-8-sig') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        pos_data.append([float(value) for value in row])


fov = 75.0

pi = 3.14159265

scene = bpy.context.scene

# Set render resolution
scene.render.resolution_x = 512
scene.render.resolution_y = 512

# Set camera fov in degrees
scene.camera.data.angle = fov*(pi/180.0)

# stating index in pos_data
point = 0

# Set everything to quaternion mode
bpy.data.objects['Start Point'].rotation_mode = 'QUATERNION'
bpy.data.objects['End Point'].rotation_mode = 'QUATERNION'
scene.camera.rotation_mode = 'QUATERNION'

# set start and end to the first two points from pos_data
bpy.data.objects['Start Point'].location = mathutils.Vector((pos_data[point][0], pos_data[point][1], pos_data[point][2]))
bpy.data.objects['End Point'].location = mathutils.Vector((pos_data[point+1][0], pos_data[point+1][1], pos_data[point+1][2]))
start_quat = mathutils.Euler((math.radians(pos_data[point][3]), math.radians(pos_data[point][4]), math.radians(pos_data[point][5])), 'XYZ').to_quaternion()
end_quat = mathutils.Euler((math.radians(pos_data[point+1][3]), math.radians(pos_data[point+1][4]), math.radians(pos_data[point+1][5])), 'XYZ').to_quaternion()
bpy.data.objects['Start Point'].rotation_quaternion = start_quat
bpy.data.objects['End Point'].rotation_quaternion = end_quat


# get start and end pos and rot from start and end objects
start_point = bpy.data.objects['Start Point'].location
end_point = bpy.data.objects['End Point'].location
start_rot = bpy.data.objects['Start Point'].rotation_quaternion
end_rot = bpy.data.objects['End Point'].rotation_quaternion

steps = 1
step = 0
image_num = 0

# start a timer
bpy.app.timers.register(camera_step)


"""
if __name__ == "__main__":
"""

