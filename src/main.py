import sys
import argparse

from gooey import Gooey, GooeyParser

from SettingFileReader import *


@Gooey(advanced=True , show_config=True, program_name='Timelapse Composer', default_size=(500, 800), required_cols=1, optional_cols=1, dump_build_config=False )

def main():

    # get some settings from setting file
    settings = SettingFileReader()
    defaultOutput = settings.getSetting("defaultSettings", "output")
    defaultWidth = settings.getSetting("defaultSettings", "width")
    defaultFramerate = settings.getSetting("defaultSettings", "framerate")
    defaultBitrateKb = settings.getSetting("defaultSettings", "bitratekb")



    description = "Compose a timelapse movie from a sequence of jpg images"

    #parser = argparse.ArgumentParser(description=description)
    parser = GooeyParser(description=description)

    parser.add_argument('-input', required=True, type=argparse.FileType('r'), help='A jpeg file from the sequence' , widget="FileChooser")
    parser.add_argument('-output', required=False, default=defaultOutput, help='Output sequence file name (default : ' + defaultOutput + ')' )
    parser.add_argument('-width', required=False, default=defaultWidth, type=int, help='With of the output sequence (default : ' + str(defaultWidth) + ')' )
    parser.add_argument('-height', required=False, type=int, help='height of the output sequence (default : keeps proportion to width)' )
    parser.add_argument('-framerate', required=False, default=defaultFramerate, type=int, help='Framerate of the output sequence (default : ' + str(defaultFramerate) + ')' )
    parser.add_argument('-bitrate', required=False, default=1920, type=int, help='Bitrate of the output sequence in kb/s (default : ' + str(defaultBitrateKb) + 'kb/s)' )

    args = parser.parse_args()


    print args.input.name
    print args.output
    print args.width
    print args.height
    print args.framerate
    print args.bitrate







if __name__ == '__main__':

    # gives priority to local libs
    sys.path.insert(0, "./lib/python")

    main()
