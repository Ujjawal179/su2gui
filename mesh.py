# mesh gittree menu

# definition of ui_card
from uicard import ui_card, ui_subcard, server
from trame.widgets import vuetify
from su2_json import *
from materials import *

state, ctrl = server.state, server.controller

############################################################################
# Mesh models - list options #
############################################################################
 #

###############################################################
# PIPELINE CARD : MESH
###############################################################

def mesh_card():
    with ui_card(title="Mesh", ui_name="Mesh"):
        print("## Mesh Selection ##")
        vuetify.VTextarea(
                label="mesh info:",
                rows="5",
                v_model=("meshText", "blablabla"),
        )

###############################################################
# PIPELINE SUBCARD : MESH
###############################################################
# secondary card
def mesh_subcard():

    # for the card to be visible, we have to set state.active_sub_ui = "submesh_none"
    with ui_subcard(title="no mesh submodels", sub_ui_name="submesh_none"):
       vuetify.VTextarea(
                label="no mesh submodels:",
                rows="5",
                v_model=("submodeltext", "no mesh submodel"),
        )