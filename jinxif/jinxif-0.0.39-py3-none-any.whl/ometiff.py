
import aicsimageio  # Allen Institute for Cell Science Image io
from aicsimageio import AICSImage
from aicsimageio.readers.ome_tiff_reader import OmeTiffReader
from aicsimageio.writers.ome_tiff_writer import OmeTiffWriter

import ome_types  # Talley Lambert


# damir
# bue 20200421: add PATH for batch-cycif2ometiff
#export PATH=/home/groups/graylab_share/local/bin:$PATH
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/groups/graylab_share/local/lib
+ batchname
+ chin lab
+ batch date
+ slide (basename)
+ mscene
+ pxscene
+ marker
+ round
+ channel
+ exposure time
+ scene position (coordinate)
+ tma coordinate
+ pixel spaceing


   <Instrument ID="Instrument:0">
      <Microscope Type="Upright" Model="Axio Scan.Z1" Manufacturer="Carl Zeiss"/>
      <Detector ID="Detector:0" Type="CMOS" Model="HDCamC11440-22C" Manufacturer="Hamamatsu"/>
      <Objective ID="Objective:1" Model="Plan-Apochromat 20x/0.8 M27" Immersion="Air" LensNA="0.8" NominalMagnification="20.0" WorkingDistance="610.0"/>
   </Instrument>\n"""


#from ome_types.model import Instrument, Microscope, Objective, InstrumentRef


#import numpy as np
# add channel_names (marker names), channel_colors ~ ome standard but will be repetive, image_name ~ ome stanard, physical_pixel_sizes to metadata!
OmeTiffWriter.save(ai_img, 'abc.ome.tiff', dim_order='ZCYX', ome_xml=o_metaxml)


<!--
Annotatable objects
       Annotation
       Channel
       Dataset
       Experimenter
       ExperimenterGroup
       Folder
       Image
       Node
       OriginalFile
       Pixels
       PlaneInfo
       Plate
       Project
       Reagent
       Roi
       Screen
       ScreenAcquisition
       Session
       Well
       WellSample
Node ?
OriginalFile ?
Session ?
PlaneInfo (as Plane)
-->

