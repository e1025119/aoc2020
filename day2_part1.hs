import System.IO
import qualified Data.List.Split as S
import qualified Data.Text as T

main = do
    f <- openFile "in_2.txt" ReadMode
    content <- hGetContents f
    let l = lines content
    print (countPW l)
    
countPW :: [String] -> Int
countPW (x:xs) = if b >= getLower a && b <= getHigher a then 1 + (countPW xs) else 0 + (countPW xs)
    where
        a = (head (S.splitOn ":" x))
        b = (countLine x)
countPW [] = 0

countLine :: String -> Int
countLine s = length (filter (==(last (last (words (head a))))) (last a))  where a = (S.splitOn ":" s)

getLower :: String -> Int
getLower s = read (head (S.splitOn "-" (head (words s)))) :: Int

getHigher :: String -> Int
getHigher s = read (head (words (last (S.splitOn "-" (head (words s)))))) :: Int
