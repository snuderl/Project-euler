
import Data.Bits
import Data.Char
import Data.List
import qualified Data.Text as T

import Text.Regex.Posix


xor (a, b) = chr $ Data.Bits.xor o1 o2
  where o1 = ord a
        o2 = ord b


generate :: [Char] -> [Char] -> [Char]
generate txt key = map Main.xor (zip txt (cycle key))

cond str = (not (isInfixOf "{" str)) && (not (isInfixOf "^" str)) && (not (isInfixOf ":" str)) && (not (isInfixOf "&" str)) && (not (isInfixOf "%" str)) && (not (isInfixOf "$" str)) && (not (isInfixOf "`" str)) && (not (isInfixOf "~" str))

toInt :: [String] -> Char
toInt x = chr (read (head x) :: Int)

generatePermutations = [[a]++[b]++[c] | a <- ['a'..'z'], b <- ['a'..'z'], c <- ['a'..'z']]

main = do
  contents <- readFile "cipher1.txt"
  let txt = map toInt (contents =~ "[0-9]+" :: [[String]])
  let filtered = filter cond (map (generate txt) generatePermutations)
  putStrLn $ show $ sum $ map ord (filtered !! 0)


