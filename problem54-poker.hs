import qualified Data.Text as T

main = do
  content <- readFile "poker.txt"
  let fileLines = lines content
  let b = length fileLines
  putStrLn $ show $ calcHands $ fileLines !! 0
  return ()


numbers = ["2","3","4","5","6","7","8","9","J","Q","K","A"]

calcHands :: String -> ([String],[String])
calcHands line = ([bestMove player1],player2)
  where cards = map T.unpack $ T.splitOn (T.pack " ") (T.pack line)
        player1 = take 5 cards
        player2 = drop 5 cards

bestMove cards = numbers
  where colors = map (!! 1) cards
        numbers = map (!! 0) cards