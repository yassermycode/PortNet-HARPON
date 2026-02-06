import Navbar from './Navbar';

<<<<<<< HEAD
const Layout = ({ children, fullWidth = false }) => {
  if (fullWidth) {
    return (
      <div className="min-h-screen">
        <Navbar />
        {children}
      </div>
    );
  }

=======
const Layout = ({ children }) => {
>>>>>>> 2e9ad4fb2de1d57abec05a2a6cf91d4a88bd05e4
  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {children}
      </main>
    </div>
  );
};

export default Layout;
