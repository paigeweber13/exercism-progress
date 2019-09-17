module LeapYear (isLeapYear) where

isLeapYear :: Integer -> Bool
isLeapYear year
  | not (mod year 100 == 0) && mod year 4 == 0 = True
  | mod year 100 == 0 && mod year 400 == 0 = True
  | otherwise = False
