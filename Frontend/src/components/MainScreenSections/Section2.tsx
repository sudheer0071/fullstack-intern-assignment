import { useEffect, useState } from "react"
import axios from "axios"
import { Send } from "lucide-react" 
import { BACKEND_URL, BOTIMG } from "../../utils/config";
import { useChatScroll } from "../../hooks/useChatScroll";
import { toast, Toaster } from "sonner";
 

export const Section2 = () => {
  const [words, setWords] = useState([]);
  const [typereffect, setTyperEffect] = useState('')
  const [currentIndex, setCurrentIndex] = useState(0)
  const [input, setInput] = useState('')

  const [messages, setMessages] = useState<{ text: string; sender: string; }[]>([]);
  const [latestBotMessageIndex, setLatestBotMessageIndex] = useState(-1);

  const ref = useChatScroll(messages)


  useEffect(() => {
    if (words.length == 0) {
      setTyperEffect(' ')
      return;
    }
    // let currentIndex = 0
    const interval = setInterval(() => {
      if (currentIndex < words.length) {
        const nextword = words[currentIndex];
        setTyperEffect((prev) => prev + "" + nextword)
        setCurrentIndex((prev) => prev + 1)
      } else {
        clearInterval(interval)
      }
    }, 5);
    return () => clearInterval(interval)
  }, [words, currentIndex])


  const fetchResponse = async () => {
    if (input == '') {
      toast.warning("Please enter response first.")
      return
    }
    else {
      const toastRes =  toast.loading("Generating response...")
      try {
        console.log("inside main fetch 1");

        const res = await axios.get(
          `${BACKEND_URL}/chat/`, {
          params: { query: input }
        }
        );
        const message = await res.data.answer 
        setMessages([...messages, { text: input, sender: 'user' }, { text: message, sender: 'bot' }]);
        console.log(message);
        setLatestBotMessageIndex(messages.length)
        console.log("latest bot message index: " + latestBotMessageIndex); 
        toast.dismiss(toastRes)
        setWords(message)
        setTyperEffect('')
        setCurrentIndex(0)
        setInput('')
      } catch (error) {
        console.error(error)
        toast.dismiss(toastRes)
      }
    }

  }


  return (
    <section className=" relative flex-1 h-full w-full overflow-auto " >
      <div role="presentation" tabIndex={0} className="  flex h-full flex-col">
        <div className=" lg:px-10 ">
          <div>
            <div className=" flex-1 overflow-hidden text-slate-600 md:px-6 lg:px-10 mt-20 md:mt-40 lg:mt-40 pb-32 w-full">
              <Toaster position="top-right" richColors />
              {<div id="pdf-content" ref={ref} className=" " >
                <div id="messages" className=" ">

                  {messages.map((message, index) => (
                    <div key={index} className={`message ${message.sender === 'user' ? ' rounded-lg p-1 md:p-2 lg:p-2 mld-auto text-black font-medium mx-4 mt-3' : ' rounded-lg  md:p-2  lg:p-2 ml-  text-black mx-4 mt-10 lg:text-lg font-normal'}`}>
                      {message.sender == 'bot' && index === latestBotMessageIndex + 1 ? (
                        <span className=" flex gap-4 md:gap-6 lg:gap-7">
                          <div className=" size-10 md:size-11 lg:size-11 ">
                            <img width={45} src={BOTIMG} alt="" className=" " />
                          </div>
                          <div className=" space-y-2 w-full">
                            {typereffect.split('\n').map((line, index) => <p>
                              {line.split('/n').map((word, wordIndex) => {
                                const mainWord = word.split(')')

                                {/* if there is any links in the response by bot */ }
                                const words = mainWord[0]
                                const urlRegex = /((?:\[|\()*)(https?:\/\/\S+)((?:\]|\))*)/i;
                                const match = words.match(urlRegex);
                                if (match) {
                                  return (
                                    <div key={wordIndex}>
                                      {mainWord[0].split("]")[0]}{"]"}
                                      <span className=" ml-4 font-mono text-blue-700" key={`${index}-${wordIndex}`}>
                                        {match[1]}
                                        <a href={match[2]} target="_blank" rel="noopener noreferrer">
                                          {match[2]}{")"}
                                        </a>
                                        {/* {match[3]}{' '} */}
                                      </span>
                                      <div>
                                        {mainWord[1] && mainWord[1].split(/[:\-]/)}
                                      </div>
                                    </div>
                                  );
                                } else {
                                  return <span key={`${index}-${wordIndex}`}>{word} </span>;
                                }
                              })}
                            </p>)}
                          </div>
                        </span>
                      ) : (
                        message.text.split('\n').map((line, index) => (
                        <span className="flex  gap-4 md:gap-6 lg:gap-7">
                          {message.sender == 'bot' ?
                          
                           index == 0 ?  
                          <div className=" size-10 md:size-11 lg:size-11  " > 
                           <img width={90} src={BOTIMG} alt="" /> 
                           </div> 
                           :
                            <div className=" w-[40px] md:w-[44px] lg:w-[44px]"></div>
                            :
                             <div className={`items-center text-center bg-[#B0ACE9] rounded-full size-8 md:size-10 lg:size-10 md:text-xl lg:text-xl text-white`}>
                               <div className=' flex justify-center mt-1 md:mt-1 lg:mt-1'>
                                </div>S</div>}
                             <div className="  mt-2 w-full"> <p>
                              {line.split(' ').map((word, wordIndex) => {
                                const mainWord = word.split(')')
                                const words = mainWord[0]
                                const urlRegex = /((?:\[|\()*)(https?:\/\/\S+)((?:\]|\))*)/i;
                                const match = words.match(urlRegex);
                                if (match) {
                                  return (
                                    <div key={wordIndex}>
                                      {mainWord[0].split("]")[0]}{"]"}
                                      <span className=" ml-4 font-mono text-blue-700" key={`${index}-${wordIndex}`}>
                                        {match[1]}
                                        <a href={match[2]} target="_blank" rel="noopener noreferrer">
                                          {match[2]}{")"}
                                        </a>
                                        {/* {match[3]}{' '} */}
                                      </span>
                                      <div>
                                        {mainWord[1].split(":")}
                                      </div>
                                    </div>
                                  );
                                } else {
                                  return <span key={`${index}-${wordIndex}`}>{word} </span>;
                                }
                              })}
                             </p>
                            
                          </div>
                        </span>
                        ))
                      )}
                    </div>
                  ))}
                </div>
              </div>}
            </div>
          </div>
        </div>

        <div className=" fixed bottom-0 pb-5 md:pb-10 lg:pb-14 px-4 md:px-20 lg:px-24 bg-white w-full">
          <div>
            <div className="flex items-center border-2 shadow-md rounded-lg py-4 px-8">
              <input
                type="text"
                placeholder="Send a message..."
                onKeyDown={(e: React.KeyboardEvent<HTMLInputElement>) => {
                  if (e.key === 'Enter') {
                    fetchResponse();
                  }
                }}
                value={input}
                onChange={(e) => setInput(e.target.value)}
                className="flex-1 text-base bg-transparent focus:outline-none font-medium"
              />
              <button onClick={fetchResponse} type="submit" className="text-[#222222]">
                <Send size={24} />
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );

}
