import { FileUpload } from "../FileUpload"

 
export const Section1 = ()=>{
  return <section  className=" z-[99] bg-white fixed w-full border-b-2 shadow-md">
 
    <div className=" containers flex justify-between items-center">
    <div className=" flex h-full">
      <a href="/">
       <img src="AI Planet Logo.png" alt="" className=" w-[80px] md:w-full lg:w-full" />
      </a>
    </div>

    <div className="">
       <FileUpload/>
    </div>
    </div>
  </section>
}