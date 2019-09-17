module LeapYear (isLeapYear) where

-- adopted solution by acamino because it's beautifully expressive
-- https://exercism.io/tracks/haskell/exercises/leap/solutions/eed4277a70a24fb6af10bd5335053dfe
isLeapYear :: Integer -> Bool
isLeapYear year
  | isDivisibleBy 400 = True
  | isDivisibleBy 100 = False
  | isDivisibleBy 4 = True
  | otherwise = False
  where isDivisibleBy x = mod year x == 0
