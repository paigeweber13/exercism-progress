module LeapYear (isLeapYear) where

-- adopted solution by acamino because it's beautifully expressive
-- https://exercism.io/tracks/haskell/exercises/leap/solutions/eed4277a70a24fb6af10bd5335053dfe
isLeapYear :: Integer -> Bool
isLeapYear year
  -- conditional'
  -- the below stuff with the pipe symobls is what is called a 'guarded
  | year `isDivisibleBy` 400 = True
  | year `isDivisibleBy` 100 = False
  | year `isDivisibleBy` 4 = True
  | otherwise = False
  where isDivisibleBy x y = mod x y == 0
