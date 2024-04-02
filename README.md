# Chameleon_fabric
This documentation explains the functionality and usage of a Python script for Blender. The script utilizes the Blender Python API (`bpy`) to perform various operations such as importing FBX files, positioning objects, modifying materials, iterating through collections, and exporting to FBX format.

## Functions

### 1. `import_and_position_fbx(fbx_file_path, new_position)`

This function imports an FBX file and positions the imported object at the specified location.

- `fbx_file_path`: Path to the FBX file to be imported.
- `new_position`: Tuple representing the new position coordinates `(x, y, z)`.

### 2. `Tank(material, image_path)`

This function modifies the material of an object by adding an image texture to the base color.

- `material`: Material to be modified.
- `image_path`: Path to the texture image file.

### 3. `iterate_materials_in_collection(collection)`

This function iterates through the materials of objects within a collection and applies the `Tank` function to each material.

- `collection`: Collection to iterate through.

### 4. `iterate_collections()`

This function iterates through all collections in the scene's top-level collection and calls `iterate_materials_in_collection` for each collection.

### 5. `export_final_collections_to_fbx(fbx_export_path)`

This function exports the final edited collections to an FBX file.

- `fbx_export_path`: Path to save the edited FBX file.

## Example Usage

```python
# Example usage:
fbx_file_path = "Path_of_fbxfile"
new_position = (0.117032, 1.58816e-06, -11.8203)
import_and_position_fbx(fbx_file_path, new_position)

iterate_collections()

fbx_export_path = "Path_to_save_edited_fbx_file"
export_final_collections_to_fbx(fbx_export_path)
