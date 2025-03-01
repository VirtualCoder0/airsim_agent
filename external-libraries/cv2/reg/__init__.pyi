import cv2
import cv2.typing
import typing


# Classes
class Map:
    # Functions
    @typing.overload
    def warp(self, img1: cv2.typing.MatLike, img2: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @typing.overload
    def warp(self, img1: cv2.UMat, img2: cv2.UMat | None = ...) -> cv2.UMat: ...

    @typing.overload
    def inverseWarp(self, img1: cv2.typing.MatLike, img2: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @typing.overload
    def inverseWarp(self, img1: cv2.UMat, img2: cv2.UMat | None = ...) -> cv2.UMat: ...

    def inverseMap(self) -> Map: ...

    def compose(self, map: Map) -> None: ...

    def scale(self, factor: float) -> None: ...


class Mapper:
    # Functions
    @typing.overload
    def calculate(self, img1: cv2.typing.MatLike, img2: cv2.typing.MatLike, init: Map = ...) -> Map: ...
    @typing.overload
    def calculate(self, img1: cv2.UMat, img2: cv2.UMat, init: Map = ...) -> Map: ...

    def getMap(self) -> Map: ...


class MapTypeCaster:
    # Functions
    @staticmethod
    def toAffine(sourceMap: Map) -> MapAffine: ...

    @staticmethod
    def toShift(sourceMap: Map) -> MapShift: ...

    @staticmethod
    def toProjec(sourceMap: Map) -> MapProjec: ...


class MapAffine(Map):
    # Functions
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, linTr: cv2.typing.MatLike, shift: cv2.typing.MatLike) -> None: ...
    @typing.overload
    def __init__(self, linTr: cv2.UMat, shift: cv2.UMat) -> None: ...

    @typing.overload
    def inverseWarp(self, img1: cv2.typing.MatLike, img2: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @typing.overload
    def inverseWarp(self, img1: cv2.UMat, img2: cv2.UMat | None = ...) -> cv2.UMat: ...

    def inverseMap(self) -> Map: ...

    def compose(self, map: Map) -> None: ...

    def scale(self, factor: float) -> None: ...

    @typing.overload
    def getLinTr(self, linTr: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @typing.overload
    def getLinTr(self, linTr: cv2.UMat | None = ...) -> cv2.UMat: ...

    @typing.overload
    def getShift(self, shift: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @typing.overload
    def getShift(self, shift: cv2.UMat | None = ...) -> cv2.UMat: ...


class MapperGradAffine(Mapper):
    # Functions
    def __init__(self) -> None: ...

    @typing.overload
    def calculate(self, img1: cv2.typing.MatLike, img2: cv2.typing.MatLike, init: Map = ...) -> Map: ...
    @typing.overload
    def calculate(self, img1: cv2.UMat, img2: cv2.UMat, init: Map = ...) -> Map: ...

    def getMap(self) -> Map: ...


class MapperGradEuclid(Mapper):
    # Functions
    def __init__(self) -> None: ...

    @typing.overload
    def calculate(self, img1: cv2.typing.MatLike, img2: cv2.typing.MatLike, init: Map = ...) -> Map: ...
    @typing.overload
    def calculate(self, img1: cv2.UMat, img2: cv2.UMat, init: Map = ...) -> Map: ...

    def getMap(self) -> Map: ...


class MapperGradProj(Mapper):
    # Functions
    def __init__(self) -> None: ...

    @typing.overload
    def calculate(self, img1: cv2.typing.MatLike, img2: cv2.typing.MatLike, init: Map = ...) -> Map: ...
    @typing.overload
    def calculate(self, img1: cv2.UMat, img2: cv2.UMat, init: Map = ...) -> Map: ...

    def getMap(self) -> Map: ...


class MapperGradShift(Mapper):
    # Functions
    def __init__(self) -> None: ...

    @typing.overload
    def calculate(self, img1: cv2.typing.MatLike, img2: cv2.typing.MatLike, init: Map = ...) -> Map: ...
    @typing.overload
    def calculate(self, img1: cv2.UMat, img2: cv2.UMat, init: Map = ...) -> Map: ...

    def getMap(self) -> Map: ...


class MapperGradSimilar(Mapper):
    # Functions
    def __init__(self) -> None: ...

    @typing.overload
    def calculate(self, img1: cv2.typing.MatLike, img2: cv2.typing.MatLike, init: Map = ...) -> Map: ...
    @typing.overload
    def calculate(self, img1: cv2.UMat, img2: cv2.UMat, init: Map = ...) -> Map: ...

    def getMap(self) -> Map: ...


class MapperPyramid(Mapper):
    numLev_: int
    numIterPerScale_: int

    # Functions
    def __init__(self, baseMapper: Mapper) -> None: ...

    @typing.overload
    def calculate(self, img1: cv2.typing.MatLike, img2: cv2.typing.MatLike, init: Map = ...) -> Map: ...
    @typing.overload
    def calculate(self, img1: cv2.UMat, img2: cv2.UMat, init: Map = ...) -> Map: ...

    def getMap(self) -> Map: ...


class MapProjec(Map):
    # Functions
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, projTr: cv2.typing.MatLike) -> None: ...
    @typing.overload
    def __init__(self, projTr: cv2.UMat) -> None: ...

    @typing.overload
    def inverseWarp(self, img1: cv2.typing.MatLike, img2: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @typing.overload
    def inverseWarp(self, img1: cv2.UMat, img2: cv2.UMat | None = ...) -> cv2.UMat: ...

    def inverseMap(self) -> Map: ...

    def compose(self, map: Map) -> None: ...

    def scale(self, factor: float) -> None: ...

    @typing.overload
    def getProjTr(self, projTr: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @typing.overload
    def getProjTr(self, projTr: cv2.UMat | None = ...) -> cv2.UMat: ...

    def normalize(self) -> None: ...


class MapShift(Map):
    # Functions
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, shift: cv2.typing.MatLike) -> None: ...
    @typing.overload
    def __init__(self, shift: cv2.UMat) -> None: ...

    @typing.overload
    def inverseWarp(self, img1: cv2.typing.MatLike, img2: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @typing.overload
    def inverseWarp(self, img1: cv2.UMat, img2: cv2.UMat | None = ...) -> cv2.UMat: ...

    def inverseMap(self) -> Map: ...

    def compose(self, map: Map) -> None: ...

    def scale(self, factor: float) -> None: ...

    @typing.overload
    def getShift(self, shift: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @typing.overload
    def getShift(self, shift: cv2.UMat | None = ...) -> cv2.UMat: ...



