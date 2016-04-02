# ADDS A PANEL IN TOOLS MENU. 


import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "TestPanel"
    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "TestPanel"
    bl_context = "objectmode"
    bl_label = "TESTPANEL101"
    
    bl_idname = "PANEL_PT_TestPanel"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Hi This is first panel: Yeah")

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.operator("mesh.primitive_cube_add")


def register():
    bpy.utils.register_class(TestPanel)


def unregister():
    bpy.utils.unregister_class(TestPanel)


if __name__ == "__main__":
    register()
