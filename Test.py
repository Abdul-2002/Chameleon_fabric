import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)


def import_and_position_fbx(fbx_file_path, new_position):
    # Importing FBX file
    bpy.ops.import_scene.fbx(filepath=fbx_file_path)

    # Changing the position of the object to the specified new_position
    bpy.ops.transform.translate(value=new_position, orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)

    # Removing the camera and light source
    for obj in bpy.context.scene.objects:
        if obj.type == 'CAMERA' or obj.type == 'LIGHT':
            obj.select_set(True)
        else:
            obj.select_set(False)
    bpy.ops.object.delete()

def Tank(material, image_path):
    if material is not None:
        # Ensure the material is assigned to an object
        if material.users > 0:
            # Access the material nodes
            nodes = material.node_tree.nodes

            # Find the principled BSDF node
            principled_node = nodes.get("Principled BSDF")

            if principled_node is not None:
                # Create an Image Texture node
                image_texture_node = nodes.new(type='ShaderNodeTexImage')

                # Load the image
                image_texture = bpy.data.images.load(image_path)
                image_texture_node.image = image_texture

                # Connect the Image Texture node to the Base Color input
                material.node_tree.links.new(image_texture_node.outputs['Color'], principled_node.inputs['Base Color'])

            else:
                print("Principled BSDF node not found in material.")

        else:
            print("Material is not assigned to any objects.")
    else:
        print("Material not found.")

def iterate_materials_in_collection(collection):
    # Iterate over materials of objects in the given collection
    for obj in collection.objects:
        if obj.type == 'MESH':
            for slot in obj.material_slots:
                if slot.material is not None:
                    Tank(slot.material, "Path_of_the_texture_image")  # Replace with your image file path

def iterate_collections():
    # Iterate through all collections in the scene's top-level collection (screen collection)
    for collection in bpy.context.scene.collection.children:
        iterate_materials_in_collection(collection)

def export_final_collections_to_fbx(fbx_export_path):
    bpy.ops.object.select_all(action='SELECT')  # Select all objects in the scene
    if bpy.context.selected_objects:
        bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]
        bpy.ops.export_scene.fbx(filepath=fbx_export_path, use_selection=True)
        print("Export successful!")
    else:
        print("No objects selected. Please select the object(s) you want to export.")

# Example usage:
fbx_file_path = "Path_of_fbxfile"
new_position = (0.117032, 1.58816e-06, -11.8203)
import_and_position_fbx(fbx_file_path, new_position)
iterate_collections()

fbx_export_path = "Path_to_save_edited_fbx_file"
export_final_collections_to_fbx(fbx_export_path)
