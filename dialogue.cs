using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Dialogue : MonoBehaviour {

	// Use this for initialization
	void Start () {
		List<string> input = new List<string>();
		input.Add("START");
		getnext (input);
	}
	// Update is called once per frame
	void Update () {
	}

	public List<string> getnext(List<string> input){

		string nextNode = "NONE";
		string nextText = "NONE";

		//to be populated...
		string currentNode = input [0];
		string UserName = "Amir";
		string AnalysisCustSingle = "extrovert";
		string UserInterest = "the matrix";
		string AnalysisBasic = "gmail.com";
		string MicSpeech = "";
		string FCamEmotion = "";
		string AnalysisCustMult = "";
		string UIKeyboard = "";

		bool IsConditional = false;
		bool IsAvatarNode = false;
		bool IsRandom = false;
		bool IsSpecific = false;
		bool MicSpeechFlag1 = false;
		bool FCamEmotionFlag1 = false;
		bool AnalysisBasicFlag1 = false;
		bool AnalysisCustSingleFlag1 = false;
		bool AnalysisCustMultFlag1 = false;
		bool UIKeyboardFlag1 = false;
		bool MicSpeechFlag2 = false;
		bool FCamEmotionFlag2 = false;
		bool AnalysisBasicFlag2 = false;
		bool AnalysisCustSingleFlag2 = false;
		bool AnalysisCustMultFlag2 = false;
		bool UIKeyboardFlag2 = false;
		bool UserResponse1 = false;
		bool UserResponse2 = false;

		string AvatarFace = "NONE";
		string AvatarBody = "NONE";
		string AvatarVoice = "NONE";
		string SceneRendering = "NONE";
		string SceneSound = "NONE";
		string NarratorSound = "NONE";
		string GUIScreen = "NONE";

		if(currentNode == "NONE") {
			List<string> output = new List<string> ();
			print ("END");
			output.Add ("END");
			output.Add ("END");
			output.Add ("END");
			output.Add ("END");
			output.Add ("END");
			output.Add ("END");
			output.Add ("END");
			output.Add ("END");
			output.Add ("END");
			return output;

		}else {

			if(currentNode == "START"){
				IsAvatarNode = true; 
				nextText = "Hello " + UserName + " " ;
				AvatarFace =  "NONE";
				AvatarBody =  "NONE";
				AvatarVoice =  "NONE";
				SceneRendering =  "NONE";
				SceneSound =  "NONE";
				NarratorSound =  "NONE";
				GUIScreen =  "NONE";
				nextNode = "Avatar1";
			}

			if(currentNode == "Avatar1"){
				IsAvatarNode = true; 
				nextText = "I love the fact that you are an " + AnalysisCustSingle + " ";
				AvatarFace =  "Smiling ";
				AvatarBody =  "NONE";
				AvatarVoice =  "NONE";
				SceneRendering =  "NONE";
				SceneSound =  "NONE";
				NarratorSound =  "NONE";
				GUIScreen =  "NONE";
				nextNode = "Avatar2";
			}

			if(currentNode == "Avatar2"){
				IsAvatarNode = true; 
				nextText = "OMG! you like " + UserInterest + " ";
				AvatarFace =  "NONE";
				AvatarBody =  "Jumping ";
				AvatarVoice =  "NONE";
				SceneRendering =  "NONE";
				SceneSound =  "NONE";
				NarratorSound =  "NONE";
				GUIScreen =  "NONE";
				nextNode = "Avatar3";
			}

			if(currentNode == "Avatar3"){
				IsAvatarNode = true; 
				nextText = "Are you still using " + AnalysisBasic + " ? ";
				AvatarFace =  "NONE";
				AvatarBody =  "NONE";
				AvatarVoice =  "NONE";
				SceneRendering =  "NONE";
				SceneSound =  "NONE";
				NarratorSound =  "NONE";
				GUIScreen =  "NONE";
				nextNode = "Logic";
			}

			if(currentNode == "Logic"){
				IsAvatarNode = false; 
				IsRandom = false;
				IsSpecific = false;
				IsConditional = true;
				MicSpeechFlag1 = true;
				FCamEmotionFlag1 = true;
				if(AnalysisBasic ==  "gmail.com"){AnalysisBasicFlag1 = true;}
				AnalysisCustSingleFlag1 = true;
				AnalysisCustMultFlag1 = true;
				UIKeyboardFlag1 = true;
				if(MicSpeechFlag1 && FCamEmotionFlag1 && AnalysisBasicFlag1 && AnalysisCustSingleFlag1 && AnalysisCustMultFlag1 && UIKeyboardFlag1){ UserResponse1 = true; ;}

				MicSpeechFlag2 = true;
				FCamEmotionFlag2 = true;
				if(AnalysisBasic !=  "gmail.com"){AnalysisBasicFlag2 = true;}
				AnalysisCustSingleFlag2 = true;
				AnalysisCustMultFlag2 = true;
				UIKeyboardFlag2 = true;
				if(MicSpeechFlag2 && FCamEmotionFlag2 && AnalysisBasicFlag2 && AnalysisCustSingleFlag2 && AnalysisCustMultFlag2 && UIKeyboardFlag2){ UserResponse2 = true; ;}

				if (IsConditional == true && UserResponse1 == true) { currentNode = "Avatar4";}

				if (IsConditional == true && UserResponse2 == true) { currentNode = "Avatar5";}
			}

			if(currentNode == "Avatar4"){
				IsAvatarNode = true; 
				nextText = "you are so cool! ";
				AvatarFace =  "NONE";
				AvatarBody =  "NONE";
				AvatarVoice =  "NONE";
				SceneRendering =  "NONE";
				SceneSound =  "NONE";
				NarratorSound =  "NONE";
				GUIScreen =  "NONE";
				nextNode = "Logic1";
			}

			if(currentNode == "Avatar5"){
				IsAvatarNode = true; 
				nextText = "your grandmother must have hated you ";
				AvatarFace =  "NONE";
				AvatarBody =  "NONE";
				AvatarVoice =  "NONE";
				SceneRendering =  "NONE";
				SceneSound =  "NONE";
				NarratorSound =  "NONE";
				GUIScreen =  "NONE";

			}

			if(currentNode == "Avatar6"){
				IsAvatarNode = true; 
				nextText = "I bet your grandmother loves you ";
				AvatarFace =  "Smiling ";
				AvatarBody =  "NONE";
				AvatarVoice =  "NONE";
				SceneRendering =  "NONE";
				SceneSound =  "NONE";
				NarratorSound =  "NONE";
				GUIScreen =  "NONE";

			}

			if(currentNode == "Logic1"){
				IsAvatarNode = false; 
				IsRandom = false;
				IsSpecific = false;
				IsConditional = true;
				MicSpeechFlag1 = true;
				FCamEmotionFlag1 = true;
				if(AnalysisBasic ==  "gmail.com"){AnalysisBasicFlag1 = true;}
				if(AnalysisCustSingle ==  "extrovert"){AnalysisCustSingleFlag1 = true;}
				AnalysisCustMultFlag1 = true;
				UIKeyboardFlag1 = true;
				if(MicSpeechFlag1 && FCamEmotionFlag1 && AnalysisBasicFlag1 && AnalysisCustSingleFlag1 && AnalysisCustMultFlag1 && UIKeyboardFlag1){ UserResponse1 = true; ;}

				MicSpeechFlag2 = true;
				FCamEmotionFlag2 = true;
				if(AnalysisBasic ==  "gmail.com"){AnalysisBasicFlag2 = true;}
				if(AnalysisCustSingle !=  "extrovert"){AnalysisCustSingleFlag2 = true;}
				AnalysisCustMultFlag2 = true;
				UIKeyboardFlag2 = true;
				if(MicSpeechFlag2 && FCamEmotionFlag2 && AnalysisBasicFlag2 && AnalysisCustSingleFlag2 && AnalysisCustMultFlag2 && UIKeyboardFlag2){ UserResponse2 = true; ;}

				if (IsConditional == true && UserResponse1 == true) { currentNode = "Avatar6";}

				if (IsConditional == true && UserResponse2 == true) { currentNode = "Avatar5";}
			}



			//updates state
			input [0] = currentNode;
			//recurses if current node is not an output/avatar node
			if (IsAvatarNode == false) {
				return getnext (input);
			}
			List<string> output = new List<string> ();
			output = input;
			output.Clear ();

			print (nextNode + "\t\t//nextNode");
			print (nextText + "\t//nextText");
			print (AvatarFace + "\t//AvatarFace");
			print (AvatarBody + "\t//AvatarBody");
			print (AvatarVoice + "\t//AvatarVoice");
			print (SceneRendering + "\t//SceneRendering");
			print (SceneSound + "\t//SceneSound");
			print (NarratorSound + "\t//Narratorsound");
			print (GUIScreen + "\t//GUIScreen");


			output.Add (nextNode);
			output.Add (nextText);
			output.Add (AvatarFace);
			output.Add (AvatarBody);
			output.Add (AvatarVoice);
			output.Add (SceneRendering );
			output.Add (SceneSound);
			output.Add (NarratorSound);
			output.Add (GUIScreen);
			return output;
		}
	}
}

