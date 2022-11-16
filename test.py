import unittest

from encoder import Encoder


class TestEncoder(unittest.TestCase):

    def test_encoder_1(self):
        encoder = Encoder()
        result_dict = encoder.encode(
            'While The Python Language Reference describes the exact syntax and semantics of the Python language')
        self.assertDictEqual(result_dict, {'W': [1], 'h': [2, 8, 14, 48, 82, 88], 'i': [3, 42, 74], 'l': [4, 92], 'e': [5, 9, 25, 28, 30, 32, 35, 38, 44, 49, 51, 69, 83, 99], ' ': [6, 10, 17, 26, 36, 46, 50, 56, 63, 67, 77, 80, 84, 91], 'T': [7], 'P': [11, 85], 'y': [12, 58, 86], 't': [13, 47, 55, 60, 73, 81, 87], 'o': [
                             15, 78, 89], 'n': [16, 20, 33, 59, 65, 72, 90, 94], 'L': [18], 'a': [19, 23, 53, 61, 64, 71, 93, 97], 'g': [21, 24, 95, 98], 'u': [22, 96], 'R': [27], 'f': [29, 79], 'r': [31, 41], 'c': [34, 40, 54, 75], 'd': [37, 66], 's': [39, 45, 57, 68, 76], 'b': [43], 'x': [52, 62], 'm': [70]})

    def test_decoder_1(self):
        encoder = Encoder()
        result = encoder.decode({'P': [1], 'y': [2, 25, 33, 96], 't': [3, 11, 37, 77, 91, 98, 107, 119, 122, 128], 'h': [4, 99], 'o': [5, 46, 68, 103, 113, 117, 135], 'n': [6, 13, 39, 52, 64, 86, 104, 118, 121], '’': [7], 's': [8, 10, 28, 40, 80, 83, 123, 127], ' ': [9, 18, 26, 29, 34, 45, 54, 56, 61, 67, 70, 81, 84, 94, 97, 101, 106, 112, 115, 124, 131], 'a': [12, 15, 23, 55, 63, 72, 82, 90, 108], 'd': [
                                14, 17, 59, 87, 93, 130], 'r': [16, 22, 24, 32, 50, 62], 'l': [19, 75, 102, 110, 125, 134], 'i': [20, 27, 41, 51, 58, 74, 76, 78, 85, 88, 126], 'b': [21, 95, 109, 132], 'v': [30, 42], 'e': [31, 35, 38, 43, 49, 60, 66, 79, 92, 100, 111, 120, 129, 133], 'x': [36], ',': [44], 'f': [47, 48, 69, 71, 114], 'g': [53, 65, 105], 'w': [57, 136], 'c': [73, 89, 116], '.': [137]})
        self.assertEqual(
            result, 'Python’s standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below.')

    def test_encoder_2(self):
        encoder = Encoder()
        result_dict = encoder.encode(
            'The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming.')
        self.assertDictEqual(result_dict, {'T': [1], 'h': [2, 55, 101, 116, 128, 158, 208, 213, 267], 'e': [3, 36, 45, 65, 70, 81, 109, 129, 134, 137, 144, 150, 170, 179, 191, 199, 223, 235, 262, 280, 282], ' ': [4, 12, 21, 30, 38, 47, 50, 53, 58, 66, 73, 76, 83, 97, 102, 105, 110, 114, 119, 125, 135, 138, 151, 154, 161, 174, 177, 182, 185, 193, 201, 204, 211, 216, 224, 237, 247, 251, 256, 265, 270, 276, 279, 288], 'l': [5, 25, 35, 93, 108, 123, 149, 180, 181, 190, 240, 261], 'i': [6, 18, 24, 28, 42, 48, 63, 89, 94, 107, 132, 139, 147, 196, 202, 221, 233, 243, 277, 297], 'b': [7, 22, 136, 148, 260], 'r': [8, 10, 41, 60, 130, 163, 166, 171, 195, 218, 231, 250, 258, 275, 283, 290, 293], 'a': [9, 17, 56, 67, 92, 103, 117, 141, 167, 175, 183, 214, 227, 230, 253, 268, 286, 294], 'y': [11, 78, 96, 156, 206, 255, 284, 287], 'c': [
                             13, 68, 69, 87, 100, 142, 143, 272, 273], 'o': [14, 32, 61, 75, 90, 121, 126, 153, 159, 164, 187, 209, 219, 239, 244, 249, 259, 271, 291], 'n': [15, 19, 29, 46, 49, 86, 91, 140, 160, 200, 203, 210, 228, 245, 254, 278, 298], 't': [16, 26, 43, 44, 54, 57, 74, 80, 88, 95, 115, 118, 127, 152, 157, 197, 198, 207, 212, 215, 226, 242, 266, 269], 's': [20, 37, 71, 72, 77, 79, 98, 104, 133, 145, 146, 172, 176, 184, 192, 225, 238, 246, 264], 'u': [23, 34, 85, 99, 122, 189, 241, 274], '-': [27], 'm': [31, 82, 168, 169, 186, 252, 263, 295, 296], 'd': [33, 64, 124, 188, 222, 229, 232, 236, 285], '(': [39], 'w': [40, 120, 131, 178, 194], 'C': [51], ')': [52], 'p': [59, 162, 217, 257, 289], 'v': [62, 220, 281], 'f': [84, 106, 248], 'I': [111], '/': [112], 'O': [113], 'P': [155, 205], 'g': [165, 292, 299], ',': [173], 'z': [234], '.': [300]})

    def test_decoder_2(self):
        encoder = Encoder()
        result = encoder.decode({'S': [1], 'o': [2, 6, 16, 48, 53, 77, 88, 95, 100, 132, 149, 156], 'm': [3, 15, 104, 134, 158], 'e': [4, 11, 13, 20, 25, 27, 39, 44, 50, 58, 64, 70, 74, 138, 161], ' ': [5, 8, 14, 22, 26, 37, 46, 49, 59, 63, 71, 75, 87, 90, 97, 106, 109, 121, 126, 145, 150, 167], 'f': [7, 89, 131, 141, 155], 't': [9, 34, 47, 72, 79, 85, 93, 113, 117, 130, 148, 154, 163], 'h': [10, 66, 73, 94], 's': [12, 21, 40, 105, 112, 136, 144, 171], 'd': [17, 38, 45, 62], 'u': [18, 54, 162], 'l': [
                                19, 30, 35, 83, 128, 152, 166], 'a': [23, 56, 60, 67, 80, 103, 110, 115, 122, 124, 129, 153, 165], 'r': [24, 55, 78, 99, 102, 114, 133, 157, 164], 'x': [28], 'p': [29, 76, 98, 127, 137, 151], 'i': [31, 33, 41, 82, 84, 118, 140, 142, 146], 'c': [32, 52, 69, 116, 139, 143], 'y': [36, 86, 92, 108, 125], 'g': [42, 57, 101, 120], 'n': [43, 51, 61, 65, 68, 96, 119, 147, 160], 'b': [81, 107, 111], 'P': [91, 169], 'w': [123], '-': [135, 159], 'A': [168], 'I': [170], '.': [172]})
        self.assertEqual(
            result, 'Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.')

    def test_encoder_3(self):
        encoder = Encoder()
        result_dict = encoder.encode(
            'The pydoc module automatically generates documentation from Python modules. The documentation can be presented as pages of text on the console, served to a web browser, or saved to HTML files.')
        self.assertDictEqual(result_dict, {'T': [1, 77, 183], 'h': [2, 64, 78, 133], 'e': [3, 16, 33, 35, 39, 47, 73, 79, 86, 100, 104, 106, 109, 118, 125, 134, 142, 146, 149, 158, 166, 176, 190], ' ': [4, 10, 17, 31, 41, 55, 60, 67, 76, 80, 94, 98, 101, 111, 114, 120, 123, 128, 131, 135, 144, 151, 154, 156, 160, 169, 172, 178, 181, 186], 'p': [5, 102, 115], 'y': [6, 30, 62], 'd': [7, 13, 42, 70, 81, 110, 150, 177], 'o': [8, 12, 21, 43, 53, 58, 65, 69, 82, 92, 121, 129, 137, 140, 153, 163, 170, 180], 'c': [9, 26, 44, 83, 95, 136], 'm': [11, 22, 46, 59, 68, 85], 'u': [
                             14, 19, 45, 71, 84], 'l': [15, 28, 29, 72, 141, 189], 'a': [18, 23, 27, 37, 50, 89, 96, 112, 116, 155, 174], 't': [20, 24, 38, 49, 51, 63, 88, 90, 108, 124, 127, 132, 152, 179], 'i': [25, 52, 91, 188], 'g': [32, 117], 'n': [34, 48, 54, 66, 87, 93, 97, 107, 130, 138], 'r': [36, 57, 103, 147, 162, 167, 171], 's': [40, 74, 105, 113, 119, 139, 145, 165, 173, 191], 'f': [56, 122, 187], 'P': [61], '.': [75, 192], 'b': [99, 159, 161], 'x': [126], ',': [143, 168], 'v': [148, 175], 'w': [157, 164], 'H': [182], 'M': [184], 'L': [185]})

    def test_decoder_3(self):
        encoder = Encoder()
        result = encoder.decode({'F': [1], 'o': [2, 6, 29, 41, 61, 71, 87, 95, 117, 133, 140, 164, 172, 206, 209, 222, 232, 234, 252, 257, 266, 270, 274, 294, 310, 313, 333, 336, 343, 354, 366, 377, 380, 388, 411], 'r': [3, 79, 86, 99, 125, 152, 156, 189, 199, 213, 226, 247, 256, 337, 356, 367], ' ': [4, 13, 22, 32, 36, 45, 49, 59, 73, 76, 84, 89, 93, 103, 109, 113, 121, 132, 135, 139, 147, 151, 163, 166, 170, 183, 192, 195, 201, 204, 207, 218, 224, 230, 233, 240, 242, 254, 259, 263, 269, 272, 280, 286, 291, 297, 301, 312, 315, 319, 326, 335, 338, 345, 348, 352, 359, 365, 368, 371, 375, 379, 382, 386, 393, 398], 'm': [5, 37, 64, 88, 175, 184, 186, 258, 275, 276, 339, 387, 412, 413], 'd': [7, 35, 42, 50, 58, 60, 77, 83, 94, 116, 150, 171, 208, 221, 243, 302, 344, 389], 'u': [8, 24, 63, 128, 155, 174, 288, 328, 355, 390], 'l': [9, 15, 54, 161, 181, 265, 281, 321, 362, 391], 'e': [10, 19, 38, 48, 57, 65, 78, 82, 92, 107, 112, 130, 138, 143, 153, 160, 176, 182, 185, 188, 198, 200, 228, 244, 262, 277, 284, 296, 300, 303, 318, 340, 351, 358, 363, 374, 385, 392, 396, 397, 403, 408, 414], 's': [
                                11, 17, 18, 20, 31, 43, 52, 75, 97, 157, 169, 190, 203, 211, 229, 245, 285, 289, 323, 324, 353, 395, 401, 417], ',': [12, 21, 44, 146, 217, 325, 364], 'c': [14, 26, 62, 96, 118, 144, 154, 173, 210, 223, 246, 267, 273, 320, 330, 357, 404, 410], 'a': [16, 33, 55, 68, 122, 148, 179, 237, 241, 292, 322, 369], 'f': [23, 85, 134, 165, 194, 255, 271, 304, 314, 327, 360, 381], 'n': [25, 30, 34, 66, 72, 101, 149, 177, 205, 215, 239, 253, 278, 283, 306, 311, 329, 334, 347, 400, 415], 't': [27, 39, 46, 67, 69, 90, 98, 110, 123, 124, 129, 136, 145, 168, 178, 196, 212, 225, 231, 236, 250, 260, 279, 290, 298, 308, 316, 331, 341, 349, 370, 372, 376, 383, 405, 409, 416], 'i': [28, 51, 70, 74, 80, 100, 105, 126, 158, 167, 202, 214, 227, 238, 248, 251, 282, 305, 307, 309, 332, 346, 361, 399], 'h': [40, 47, 91, 111, 137, 197, 261, 299, 317, 342, 350, 373, 384], 'p': [53, 219, 249, 378, 402], 'y': [56, 162, 220], 'v': [81, 159, 295], 'g': [102, 216, 407], '(': [104, 394, 418], '.': [106, 108, 191, 406, 421], '_': [114, 115, 119, 120], 'b': [127, 141, 180, 187, 235, 264, 293], ')': [131, 419, 420], 'j': [142, 287], 'I': [193], 'k': [268]})
        self.assertEqual(
            result, 'For modules, classes, functions and methods, the displayed documentation is derived from the docstring (i.e. the __doc__ attribute) of the object, and recursively of its documentable members. If there is no docstring, pydoc tries to obtain a description from the block of comment lines just above the definition of the class, function or method in the source file, or at the top of the module (see inspect.getcomments()).')


if __name__ == '__main__':
    unittest.main()
