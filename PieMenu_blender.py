import bpy
from bpy.types import Menu

class VIEW3D_PIE_SV_ops(bpy.types.Operator):

    bl_idname = "nodes.pie_menu_enum"
    bl_label = "Operator Label"

    mode_options = [
        ("button1", "button1", "", "CURVE_DATA", 0),
        ("button2", "button2", "", "", 1),
        ("button3", "button3", "", "", 2)
    ]

    selected_mode = bpy.props.EnumProperty(
        items=mode_options,
        description="main",
        default="button1"
    )

    def execute(self, context):
        print('added ', self.selected_mode)
        return {'FINISHED'}


class VIEW3D_PIE_template(Menu):

    bl_label = "Pan Around"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator_enum("nodes.pie_menu_enum", "selected_mode")


def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()

    bpy.ops.wm.call_menu_pie(name="VIEW3D_PIE_template")