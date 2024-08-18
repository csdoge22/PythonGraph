const SimpleNav = () => {
    return (
        <>
            <nav className="d-flex navbar navbar-expand-sm bg-light">
                <div className="container-fluid">
                    <ul className="navbar-nav">
                        <li className="navbar-item">
                            <a className="nav-link" href="/">Home</a>
                        </li>
                        <li className="navbar-item">
                            <a className="nav-link" href="/graph">Graph Interface</a>
                        </li>
                        <li className="navbar-item">
                            <a className="nav-link" href="/contact">Contact</a>
                        </li>
                    </ul>
                </div>
            </nav>
        </>
    )
}
export default SimpleNav;