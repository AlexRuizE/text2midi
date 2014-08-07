text2midi
=========

Text to midi converter. This program asks the user for a text file, which is parsed into sentences. Each token is then mapped with a simple cypher to a set of simultaneous notes (chords). The resulting file is a .mid file that can be used as rythmic and melodic input for various soft-synths or drum racks.

The mapping function follows a rudimentary cypher known as French transformation, which consists of sequentially increasing integers ranging from 60 to 86. These map onto two chromatic octaves starting in C4 and ending in C6#. The complexity of the resulting patterns can be tweaked by using different mapping functions.

The script asks for two user inputs: the name of the text file to process, and the name of the output .mid file. The executable script must be in the same folder as the text file, or a full path must be provided.

Other parameters such as track number, channel, pitch, note time and velocity can also be modified.
