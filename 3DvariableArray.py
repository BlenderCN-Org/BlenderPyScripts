bl_info = {
    "name": "Cursor Array",
    "category": "Object",
}

import bpy
from bpy import *


class ObjectCursorArray(bpy.types.Operator):
    """Object Cursor Array"""
    bl_idname = "object.cursor_array"
    bl_label = "CUBE Array"
    bl_options = {'REGISTER', 'UNDO'}
    
    scn = context.window_manager
    
    ''' IDK WHY BUT THIS WORKS ONLY IF YOU UNCOMMENT THE # below and comment the code of total below that, run it like that. And then undo the steps and run.   '''
    #total = bpy.props.IntVectorProperty(name="Steps")
    total = bpy.context.window_manager.num
    total_x = total[0]
    total_y = total[1]
    total_z = total[2]

    def execute(self, context):
        scene = context.scene
        cursor = scene.cursor_location
       
        obj = scene.objects.active

        for i in range(self.total_x):
            factor_x = i / self.total_x
          
            for j in range(self.total_y):
                factor_y=j/self.total_y
                
                for k in range(self.total_z):
                    factor_z=k/self.total_z
                    
                    obj_new = obj.copy()
                    scene.objects.link(obj_new)
                    #obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))
                    obj_new.location = obj.location 
                    obj_new.location.x += context.window_manager.Space*factor_x
                    obj_new.location.y += context.window_manager.Space*factor_y
                    obj_new.location.z += context.window_manager.Space*factor_z

        return {'FINISHED'}
    
    
class HelloWorldPanel(bpy.types.Panel):
    bl_label = "MoGraph: 3DCUBE Array Cloner"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        scn = context.window_manager
        
        layout = self.layout

        obj = context.object
        
        row = layout.row()
        row.prop(scn, "num")
 
        
        row=layout.row()
        row.prop(scn, "Space")
        
        row = layout.row()
        row.operator("object.cursor_array")



def menu_func(self, context):
    self.layout.operator(ObjectCursorArray.bl_idname)


def register():
    bpy.utils.register_class(ObjectCursorArray)
    bpy.utils.register_class(HelloWorldPanel)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
  

    bpy.utils.unregister_class(ObjectCursorArray)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    bpy.utils.unregister_class(HelloWorldPanel)

if __name__ == "__main__":
    bpy.types.WindowManager.num = bpy.props.IntVectorProperty(name="EDGE:", description = "Number of Cloner Objects to be created on an edge")
   
    bpy.types.WindowManager.Space = bpy.props.IntProperty(name="Spacing")

    register()