from collections import Counter
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        st_level = 0
        friend = [id]
        video = []
        for i in friend:
            video += watchedVideos[i] 
        old_friend = []
        while st_level < level:
            new_friend = []
            
            for f in friend: 
                new_friend += friends[f]
            
            old_friend += friend
            friend = [f for f in new_friend if f not in old_friend]
            
            video = []
           
            st_level+=1
            
            if st_level == level:
             
                for i in set(friend):
                    video += watchedVideos[i] 
       
        return [j[1] for j in sorted([[i[1],i[0]] for i in Counter(video).most_common()])]

#Runtime: 280 ms, faster than 76.47% of Python3 online submissions for Get Watched Videos by Your Friends.
#Memory Usage: 16 MB, less than 51.63% of Python3 online submissions for Get Watched Videos by Your Friends.
#Fu-Ti, Hsu 
#shifty049@gmail.com