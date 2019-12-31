module SpaceAge (Planet(..), ageOn) where

-- import Data.Map (Map)
-- import qualified Data.Map as Map

-- this is an algebraic data type: it has more than one value constructor
data Planet = Mercury
            | Venus
            | Earth
            | Mars
            | Jupiter
            | Saturn
            | Uranus
            | Neptune

secondsPerEarthYear = 31557600

ageOn :: Planet -> Float -> Float
ageOn planet seconds = 0
-- ageOn planet seconds
--   | planet == Mercury = secondsPerEarthYear / 0.2408467
