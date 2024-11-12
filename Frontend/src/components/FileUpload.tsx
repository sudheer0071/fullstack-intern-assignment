import { useCallback, useState } from "react"; 
import axios from "axios";
import {toast, Toaster} from 'sonner'
import { useDropzone } from 'react-dropzone';  
import {File} from 'lucide-react'
// import { useNavigate } from "react-router-dom";  
// import { UploadIcon } from "lucide-react"; 
// import { uploadedState } from "../pages/atom";
import { BACKEND_URL } from "../utils/config";


export function FileUpload(){  
  const[uploaded, setUploaded] = useState<boolean|null>(false)
  const[fileName, setFileName] = useState<string|null> ('')
  // const [uploaded, setUploaded] = useRecoilState(uploadedState)
   
  // const navigate = useNavigate()

  const onDrop = useCallback(async (acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    const formData = new FormData();
    formData.append('file', file);

    try {  
      toast.loading("Uploading PDF..")
       
      const response = await axios.post(`${BACKEND_URL}/upload/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',  
        }
      });
      const json = response.data.message
      console.log("upload...");
      
      console.log(response.data.message);
      toast.success(json)
      setUploaded(true)
      setFileName(file.name)
    } catch (error) {
      console.error('Error uploading file:', error);
      toast.error(`Error in Uploading: ${error}`)
    }
  }, []);
 

  const {getRootProps, getInputProps} = useDropzone({onDrop})

  return ( 
      <div className=" flex gap-5 md:gap-10 lg:gap-10 items-center">
        <Toaster richColors />
       {!uploaded  && <div className=" flex gap-2 md:gap-3 lg:gap-3 items-center">
          <File strokeWidth={1.2} className=" size-[24px]  md:size-[37px] lg:size-[37px] inline-block text-[#0FA958] border p-[6px] rounded-md border-[#0FA958]"/> 
          <p className="text-[#0FA958] font-semibold text-[14px] sm:text-sm md:text-base lg:text-base"> {fileName} sudheer.pdf </p>
        </div>}
    <div {...getRootProps()} className=" flex justify-center items-center border-2 border-black rounded-lg w-full py-2 px-2 md:py-2 lg:py-2 md:px-7 lg:px-8 ">
      <div className=" w-fu ll">
      <input {...getInputProps()} /> 
       <div className=" w-[13px] sm:w-full md:w-[40px] lg:w-[40px]">
       <img src="/gala_add.png" alt="" />
      </div>
      </div>

     
      <span className=" hidden md:inline lg:inline w-full text-[1rem] font-medium "> Upload PDF</span> 
      </div>
    </div>  
  );
}