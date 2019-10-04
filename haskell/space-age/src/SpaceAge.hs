module SpaceAge (Planet(..), ageOn) where

data Planet = Mercury
            | Venus
            | Earth
            | Mars
            | Jupiter
            | Saturn
            | Uranus
            | Neptune

ageOn :: Planet -> Float -> Float
ageOn planet seconds = 
  case planet of
    Mercury -> years/0.2408467 
    Venus ->   years/0.61519726
    Earth ->   years
    Mars ->    years/1.8808158
    Jupiter -> years/11.862615
    Saturn ->  years/29.447498
    Uranus ->  years/84.016846
    Neptune -> years/164.79132
  where years = seconds/31557600

-- if Planet derived Eq, you could also use the code below:

-- ageOn :: Planet -> Float -> Float
-- ageOn planet seconds
--   | planet == Mercury = years/0.2408467 
--   | planet == Venus =   years/0.61519726
--   | planet == Earth =   years
--   | planet == Mars =    years/1.8808158
--   | planet == Jupiter = years/11.862615
--   | planet == Saturn =  years/29.447498
--   | planet == Uranus =  years/84.016846
--   | planet == Neptune = years/164.79132
--   where years = seconds/31557600