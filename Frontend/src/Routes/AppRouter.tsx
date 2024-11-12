import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { MainScreen } from '../Screens/MainScreen';

const AppRouter = () => {
  return (
    <Router future={{
      v7_startTransition: true,
      v7_relativeSplatPath:true,
    }} 
    
    >
      <Routes>
        <Route index element={<MainScreen />} />
      </Routes>
    </Router>
  );
};

export default AppRouter;
