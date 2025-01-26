public class Solution {
    public IList<string> FindAllConcatenatedWordsInADict(string[] words) {
        var hash = new HashSet<string>(words);
        List<string> ans = new();
        for (int i =0;i<words.Length;i++)
        {
            hash.Remove(words[i]);
            if (Concat(words[i], hash, new Dictionary<string, bool>()))
            {
                ans.Add(words[i]);
            }
            hash.Add(words[i]);
        }

        return ans;
    }

    private bool Concat(string word,  HashSet<string> words,Dictionary<string, bool> memo)
    {
        if (word == "")
            return true;
        
        if (memo.ContainsKey(word))
            return memo[word];
        var has = false;
        for (int i=0;i<word.Length;i++)
        {
            var sub = word.Substring(0, i+1);
            if(words.Contains(sub) && Concat(word.Substring(i+1), words, memo))
            {
                has = true;
                break;
            }
        }

        memo.Add(word, has);

        return memo[word];

    }
}