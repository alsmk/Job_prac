import os 
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   
from scripts.printing_info import fetch_commit_info

class TestFetchCommitInfo(unittest.TestCase):   
    @patch('scripts.printing_info.fetch_commit_info')
    def test_fetch_commit_info(self, mock_get):
        mock_response = [
            {
                "sha": "d535302",  
                "commit": {
                    "author": {
                        "name": "Al hel md. shahriar zaman",
                        "date": "2024-09-27T12:46:50Z"
                    }
                }
            },
            {
                "sha": "e1a2b3c",
                "commit": {
                    "author": {
                        "name": "Jane Doe",
                        "date": "2024-09-26T11:30:40Z"
                    }
                }
            }
        ]
        mock_get.return_value.json.return_value = mock_response
        
        commits = fetch_commit_info()
        latest_commit = commits[0]
        
        # self.assertEqual(latest_commit['sha'], "d535302")
        self.assertEqual(latest_commit['commit']['author']['name'], "alsmk")
        # self.assertEqual(latest_commit['commit']['author']['date'], "2024-09-27T12:46:50Z")

if __name__ == '__main__':
    unittest.main()