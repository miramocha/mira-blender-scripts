import bpy
from bpy import data as D
from bpy import context as C
from mathutils import *
from math import *
from datetime import datetime
from pathlib import Path

LIGHT_SHADE_PINK = (0.987137, 0.7544, 1)
BLUE_RIM_COLOR = (0.245294, 0.60017, 1)
PURPLE_SHADE_COLOR = (0.670856, 0.619106, 1)
YELLOW_RIM_COLOR = (1, 0.789231, 0.266164)

shadeMultiplyColor = (1, 0.686808, 0.931904)
# rimColor = (0.10948, 0.0544777, 0.479285)
# rimColor = (1, 0.899034, 0.1028)
rimColor = YELLOW_RIM_COLOR
outlineColor = (0.0451938, 0.0307121, 0.11953)
shadeColor = LIGHT_SHADE_PINK
outlineWidth = 0.001
rimLightingMix = 0.25
vrmTitlePrefix = 'Mira Luna V12'

for mat in bpy.data.materials:
    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.parametric_rim_color_factor = rimColor
    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.outline_color_factor = outlineColor
    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.rim_lighting_mix_factor = rimLightingMix
    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.parametric_rim_fresnel_power_factor = 50
    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shading_shift_factor = 1
    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.gi_equalization_factor = 0.8
    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shading_toony_factor = 0.95
        
    if mat.vrm_addon_extension.mtoon1.alpha_mode != 'BLEND':
        mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.outline_width_mode = 'worldCoordinates'
        mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.outline_width_factor = outlineWidth
    if mat.vrm_addon_extension.mtoon1.emissive_texture.index.source == bpy.data.images["Shader_NoneBlack"]:
        mat.vrm_addon_extension.mtoon1.emissive_texture.index.source = bpy.data.images["v12_white_px.png"]
        mat.vrm_addon_extension.mtoon1.emissive_factor = (0, 0, 0)
        mat.vrm_addon_extension.mtoon1.extensions.khr_materials_emissive_strength.emissive_strength = 0
        
#    baseColorFactor = mat.vrm_addon_extension.mtoon1.pbr_metallic_roughness.base_color_factor
#    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shade_color_factor[0] = (shadeMultiplyColor[0] * baseColorFactor[0])
#    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shade_color_factor[1] = (shadeMultiplyColor[1] * baseColorFactor[1])
#    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shade_color_factor[2] = (shadeMultiplyColor[2] * baseColorFactor[2])
    mat.vrm_addon_extension.mtoon1.pbr_metallic_roughness.base_color_factor[0] = 1
    mat.vrm_addon_extension.mtoon1.pbr_metallic_roughness.base_color_factor[1] = 1
    mat.vrm_addon_extension.mtoon1.pbr_metallic_roughness.base_color_factor[2] = 1 
    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shade_color_factor = shadeColor

bpy.data.armatures["Armature"].vrm_addon_extension.vrm0.meta.title = vrmTitlePrefix + '_' + datetime.now().strftime('%y%m%d%H%M%S')
bpy.data.armatures["Armature"].vrm_addon_extension.vrm0.meta.version = datetime.now().strftime('%m%d%y_%H%M%S')

filename = 'V12_' + datetime.now().strftime('%m%d%y') + '.vrm'
primaryFilePath = 'D:\\art\\v12_model\\export\\' + filename
secondaryFilePath = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Warudo\\Warudo_Data\\StreamingAssets\\Characters\\' + filename

result1 = bpy.ops.export_scene.vrm(filepath=primaryFilePath)
result2 = bpy.ops.export_scene.vrm(filepath=secondaryFilePath)