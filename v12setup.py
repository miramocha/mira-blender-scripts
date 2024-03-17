import bpy
from bpy import data as D
from bpy import context as C
from mathutils import *
from math import *
from datetime import datetime

shadeMultiplyColor = (1, 0.686808, 0.931904)
rimColor = (0.10948, 0.0544777, 0.479285)
outlineColor = (0.0451938, 0.0307121, 0.11953)
shadeColor = (0.964849, 0.814811, 0.854931)
outlineWidth = 0.001
rimLightingMix = 0.25
vrmTitlePrefix = 'Mira Luna V12'

for mat in bpy.data.materials:
    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.parametric_rim_color_factor = rimColor
    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.outline_color_factor = outlineColor
    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shade_color_factor = shadeColor
    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.rim_lighting_mix_factor = rimLightingMix
        
    if mat.vrm_addon_extension.mtoon1.alpha_mode != 'BLEND':
        mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.outline_width_mode = 'worldCoordinates'
        mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.outline_width_factor = outlineWidth
    if mat.vrm_addon_extension.mtoon1.emissive_texture.index.source == bpy.data.images["Shader_NoneBlack"]:
        mat.vrm_addon_extension.mtoon1.emissive_texture.index.source = bpy.data.images["v12_white_px.png"]
        mat.vrm_addon_extension.mtoon1.emissive_factor = (0, 0, 0)
        mat.vrm_addon_extension.mtoon1.extensions.khr_materials_emissive_strength.emissive_strength = 0
    baseColorFactor = mat.vrm_addon_extension.mtoon1.pbr_metallic_roughness.base_color_factor
    mat.vrm_addon_extension.mtoon1.extensions.vrmc_materials_mtoon.shade_color_factor = (baseColorFactor[0], baseColorFactor[1], baseColorFactor[2])

bpy.data.armatures["Armature"].vrm_addon_extension.vrm0.meta.title = vrmTitlePrefix + '_' + datetime.now().strftime('%y%m%d%H%M%S')
bpy.data.armatures["Armature"].vrm_addon_extension.vrm0.meta.version = datetime.now().strftime('%m%d%y_%H%M%S')
